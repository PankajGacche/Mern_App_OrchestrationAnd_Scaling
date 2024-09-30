import boto3
import uuid

ec2 = boto3.resource('ec2')

# Create a VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{"Key": "Name", "Value": "MyVPC" + str(uuid.uuid4())[:5]}])
vpc.wait_until_available()

# Create an Internet Gateway
igw = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=igw.id)

# Create Subnets in different Availability Zones
subnet1 = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc.id, AvailabilityZone='eu-north-1a')  # Replace with your AZ
subnet2 = ec2.create_subnet(CidrBlock='10.0.2.0/24', VpcId=vpc.id, AvailabilityZone='eu-north-1b')  # Replace with your AZ

# Create a route table and add a route to the internet
route_table = ec2.create_route_table(VpcId=vpc.id)
route_table.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=igw.id
)

# Associate the route table with the subnets
route_table.associate_with_subnet(SubnetId=subnet1.id)
route_table.associate_with_subnet(SubnetId=subnet2.id)

# Create Security Group
security_group = ec2.create_security_group(GroupName='MySec' + str(uuid.uuid4())[:5], 
                                            Description='Security group for my backend', 
                                            VpcId=vpc.id)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0', 
    IpProtocol='tcp', 
    FromPort=80, 
    ToPort=80
)

security_group.authorize_ingress(
    CidrIp='0.0.0.0/0', 
    IpProtocol='tcp', 
    FromPort=22, 
    ToPort=22
)

security_group.authorize_ingress(
    CidrIp='0.0.0.0/0', 
    IpProtocol='tcp', 
    FromPort=8080, 
    ToPort=8080
)

# Define Auto Scaling Group (ASG)
client = boto3.client('autoscaling')

# Create Launch Configuration
launch_configuration_name = 'MyLaunch' + str(uuid.uuid4())[:5]
response = client.create_launch_configuration(
    LaunchConfigurationName=launch_configuration_name,
    ImageId='ami-07a0715df72e58928', 
    InstanceType='t3.micro',
    SecurityGroups=[security_group.id],
    UserData='''#!/bin/bash
                 docker run -d -p 3001:3001 mernapplication-hello
                 docker run -d -p 3002:3002 mernapplication-profile'''
)

# Create Auto Scaling Group
response = client.create_auto_scaling_group(
    AutoScalingGroupName='MyAutoSc' + str(uuid.uuid4())[:5],
    LaunchConfigurationName=launch_configuration_name,
    MinSize=1,
    MaxSize=5,
    VPCZoneIdentifier=subnet1.id + ',' + subnet2.id,
)

elbv2 = boto3.client('elbv2')

# Create Load Balancer
response = elbv2.create_load_balancer(
    Name='MyLoadBa' + str(uuid.uuid4())[:5],
    Subnets=[subnet1.id, subnet2.id],
    SecurityGroups=[security_group.id],
    Scheme='internet-facing',
    Tags=[{'Key': 'Name', 'Value': 'MyLoadBa' + str(uuid.uuid4())[:5]}],
)

route53 = boto3.client('route53')

response = route53.create_hosted_zone(
    Name='test.com'+str(uuid.uuid4())[:5], 
    CallerReference='unique-string',
    HostedZoneConfig={
        'Comment': 'Hosted zone for example.com',
        'PrivateZone': False
    }
)

# Create Frontend Launch Configuration
response = client.create_launch_configuration(
    LaunchConfigurationName='FrontendLaunchConfiguration',
    ImageId='ami-07a0715df72e58928', 
    InstanceType='t3.micro',
    SecurityGroups=[security_group.id],
    UserData='''#!/bin/bash
                 docker run -d -p 3000:3000 mernapplication-frontend'''
)

# Create Lambda function
response = lambda_client.create_function(
    FunctionName='DatabaseBackupFunction',
    Runtime='python3.8',  
    Role='arn:aws:iam::975050024946:my_lambda',  
    Handler='lambda_function.lambda_handler',
    Code={
        'ZipFile': bytes(lambda_function_code, encoding='utf-8')
    },
    Description='A function to backup the database to S3',
    Timeout=30,  # Timeout in seconds
    MemorySize=128  # Memory size in MB
)
