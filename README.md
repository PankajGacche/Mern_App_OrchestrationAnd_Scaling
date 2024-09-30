# MERN Application Deplyment
## Step 1: Set Up the AWS Environment

- 1. Set Up AWS CLI and Boto3:

   - Install AWS CLI and configure it with AWS credentials.
     ![alt text](ReadMe_Images/image.png)
   - Install Boto3 for Python and configure it.
     ![alt text](ReadMe_Images/image-1.png)

## Step 2: Prepare the MERN Application

- 1. Containerize the MERN Application:

   - Ensure the MERN application is containerized using Docker. Create a Dockerfile for each component (frontend and backend).
   ![alt text](ReadMe_Images/image-2.png)
   ![alt text](ReadMe_Images/image-3.png)

- 2. Push Docker ReadMe_Images/images to Amazon ECR:

   - Build Docker ReadMe_Images/images for the frontend and backend.
     ![alt text](ReadMe_Images/image-4.png)

   - Create an Amazon ECR repository for each ReadMe_Images/image.
     ![alt text](ReadMe_Images/image-5.png) 

   - Push the Docker ReadMe_Images/images to their respective ECR repositories.
     ![alt text](ReadMe_Images/image-6.png)
     ![alt text](ReadMe_Images/image-7.png)
     ![alt text](ReadMe_Images/image-8.png)

## Step 3: Version Control

- 1. Use AWS CodeCommit:

   - Create a CodeCommit repository.
     ![alt text](ReadMe_Images/image-9.png) 
   - Push the MERN application source code to the CodeCommit repository.
     ![alt text](ReadMe_Images/image-10.png)

## Step 4: Continuous Integration with Jenkins

- 1. Set Up Jenkins:

   - Install Jenkins on an EC2 instance.
   - Configure Jenkins with necessary plugins.
     ![alt text](ReadMe_Images/image-11.png)

- 2. Create Jenkins Jobs:

   - Create Jenkins jobs for building and pushing Docker ReadMe_Images/images to ECR.

   - Trigger the Jenkins jobs whenever there's a new commit in the CodeCommit repository.

   ![alt text](ReadMe_Images/image-12.png)
   ![alt text](ReadMe_Images/image-13.png)
   ![alt text](ReadMe_Images/image-14.png)
   ![alt text](ReadMe_Images/image-15.png)
   ![alt text](ReadMe_Images/image-16.png)

## Step 5: Infrastructure as Code (IaC) with Boto3

- 1. Define Infrastructure with Boto3 (Python Script):

   - Use Boto3 to define the infrastructure (VPC, subnets, security groups).
   - Define an Auto Scaling Group (ASG) for the backend.
   - Create AWS Lambda functions
   ![alt text](ReadMe_Images/image-17.png)
   ![alt text](ReadMe_Images/image-18.png)

## Step 6: Deploying Backend Services

- 1. Deploy Backend on EC2 with ASG:

   - Use Boto3 to deploy EC2 instances with the Dockerized backend application in the ASG.
   ![alt text](ReadMe_Images/image-19.png)

## Step 7: Set Up Networking

- 1. Create Load Balancer:

   - Set up an Elastic Load Balancer (ELB) for the backend ASG.

- 2. Configure DNS:

   - Set up DNS using Route 53 or any other DNS service.

   ![alt text](ReadMe_Images/image-20.png)

## Step 8: Deploying Frontend Services

- 1. Deploy Frontend on EC2:

   - Use Boto3 to deploy EC2 instances with the Dockerized frontend application.
   ![alt text](ReadMe_Images/image-21.png)

## Step 9: AWS Lambda Deployment

- 1. Create Lambda Functions:

- Use Boto3 to create AWS Lambda functions for specific tasks within the application.

- Backup of Db using Lambda Functions and store in S3 bucket - put time stamping on the backup

![alt text](ReadMe_Images/image-22.png)

## Step 10: Kubernetes (EKS) Deployment

- 1. Create EKS Cluster:

   - Use eksctl or other tools to create an Amazon EKS cluster.
   ![alt text](ReadMe_Images/image-23.png)
   ![alt text](ReadMe_Images/image-24.png)
   ![alt text](ReadMe_Images/image-25.png)


- 2. Deploy Application with Helm:

   - Use Helm to package and deploy the MERN application on EKS.
   ![alt text](ReadMe_Images/image-26.png)
   ![alt text](ReadMe_Images/image-27.png)
   ![alt text](ReadMe_Images/image-28.png)
## Step 11: Monitoring and Logging

- 1. Set Up Monitoring:

   - Use CloudWatch for monitoring and setting up alarms.


- 2. Configure Logging:

   - Use CloudWatch Logs or another logging solution for collecting logs.
   
   ![alt text](ReadMe_Images/image-29.png)
