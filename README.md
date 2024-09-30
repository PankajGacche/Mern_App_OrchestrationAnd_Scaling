# MERN Application Deplyment
## Step 1: Set Up the AWS Environment

- Set Up AWS CLI and Boto3:

   - Install AWS CLI and configure it with AWS credentials.
     ![alt text](ReadME_Images/image.png)
   - Install Boto3 for Python and configure it.
     ![alt text](ReadME_Images/image-1.png)

## Step 2: Prepare the MERN Application

- Containerize the MERN Application:

   - Ensure the MERN application is containerized using Docker. Create a Dockerfile for each component (frontend and backend).
   ![alt text](ReadME_Images/image-2.png)
   ![alt text](ReadME_Images/image-3.png)

- Push Docker ReadME_Images/images to Amazon ECR:

   - Build Docker ReadME_Images/images for the frontend and backend.
     ![alt text](ReadME_Images/image-4.png)

   - Create an Amazon ECR repository for each ReadME_Images/image.
     ![alt text](ReadME_Images/image-5.png) 

   - Push the Docker ReadME_Images/images to their respective ECR repositories.
     ![alt text](ReadME_Images/image-6.png)
     ![alt text](ReadME_Images/image-7.png)
     ![alt text](ReadME_Images/image-8.png)

## Step 3: Version Control

- Use AWS CodeCommit:

   - Create a CodeCommit repository.
     ![alt text](ReadME_Images/image-9.png) 
   - Push the MERN application source code to the CodeCommit repository.
     ![alt text](ReadME_Images/image-10.png)

## Step 4: Continuous Integration with Jenkins

- Set Up Jenkins:

   - Install Jenkins on an EC2 instance.
   - Configure Jenkins with necessary plugins.
     ![alt text](ReadME_Images/image-11.png)

- Create Jenkins Jobs:

   - Create Jenkins jobs for building and pushing Docker ReadME_Images/images to ECR.

   - Trigger the Jenkins jobs whenever there's a new commit in the CodeCommit repository.

   ![alt text](ReadME_Images/image-12.png)
   ![alt text](ReadME_Images/image-13.png)
   ![alt text](ReadME_Images/image-14.png)
   ![alt text](ReadME_Images/image-15.png)
   ![alt text](ReadME_Images/image-16.png)

## Step 5: Infrastructure as Code (IaC) with Boto3

- Define Infrastructure with Boto3 (Python Script):

   - Use Boto3 to define the infrastructure (VPC, subnets, security groups).
   - Define an Auto Scaling Group (ASG) for the backend.
   - Create AWS Lambda functions
   ![alt text](ReadME_Images/image-17.png)
   ![alt text](ReadME_Images/image-18.png)

## Step 6: Deploying Backend Services

- Deploy Backend on EC2 with ASG:

   - Use Boto3 to deploy EC2 instances with the Dockerized backend application in the ASG.
   ![alt text](ReadME_Images/image-19.png)

## Step 7: Set Up Networking

- Create Load Balancer:

   - Set up an Elastic Load Balancer (ELB) for the backend ASG.

- Configure DNS:

   - Set up DNS using Route 53 or any other DNS service.

   ![alt text](ReadME_Images/image-20.png)

## Step 8: Deploying Frontend Services

- Deploy Frontend on EC2:

   - Use Boto3 to deploy EC2 instances with the Dockerized frontend application.
   ![alt text](ReadME_Images/image-21.png)

## Step 9: AWS Lambda Deployment

- Create Lambda Functions:

- Use Boto3 to create AWS Lambda functions for specific tasks within the application.

- Backup of Db using Lambda Functions and store in S3 bucket - put time stamping on the backup

   ![alt text](ReadME_Images/image-22.png)

## Step 10: Kubernetes (EKS) Deployment

- Create EKS Cluster:

   - Use eksctl or other tools to create an Amazon EKS cluster.
   ![alt text](ReadME_Images/image-23.png)
   ![alt text](ReadME_Images/image-24.png)
   ![alt text](ReadME_Images/image-25.png)


- Deploy Application with Helm:

   - Use Helm to package and deploy the MERN application on EKS.
   ![alt text](ReadME_Images/image-26.png)
   ![alt text](ReadME_Images/image-27.png)
   ![alt text](ReadME_Images/image-28.png)
## Step 11: Monitoring and Logging

- Set Up Monitoring:

   - Use CloudWatch for monitoring and setting up alarms.

- Configure Logging:

   - Use CloudWatch Logs or another logging solution for collecting logs.
   
   ![alt text](ReadME_Images/image-29.png)
