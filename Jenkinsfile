pipeline {
    agent any
    environment {
        AWS_CRED = 'AWS_Credential'
        AWS_CRED_For_ECR = 'AWS_Credential_For_ECR'
        AWS_DEFAULT_REGION = 'eu-north-1'
        ECR_REPOSITORY_1 = 'pankaj_backend_hello'
        ECR_REPOSITORY_2 = 'pankaj_backend_profile'
        ECR_REPOSITORY_3 = 'pankaj_frontend'
        IMAGE_NAME_1 = 'mernapplication-hello'
        IMAGE_NAME_2 = 'mernapplication-profile'
        IMAGE_NAME_3 = 'mernapplication-frontend'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout source code
                checkout scm
                script {
                    git credentialsId: AWS_CRED, url: 'https://git-codecommit.eu-north-1.amazonaws.com/v1/repos/Mern_Repo', branch: 'master'
                    
                    // Capture the GIT_COMMIT as a local variable
                    def gitCommit = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
                    
                    // Set environment variable for later stages
                    env.GIT_COMMIT = gitCommit
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images
                    sh "docker build -t ${IMAGE_NAME_1}:${GIT_COMMIT} ./backend/helloService"
                    sh "docker build -t ${IMAGE_NAME_2}:${GIT_COMMIT} ./backend/profileService"
                    sh "docker build -t ${IMAGE_NAME_3}:${GIT_COMMIT} ./frontend"
                }
            }
        }
        stage('Login to ECR') {
            steps {
                script {
                    // Login to ECR using AWS credentials
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: AWS_CRED_For_ECR]]) {
                        def ecrLogin = sh(script: "aws ecr get-login-password --region ${AWS_DEFAULT_REGION}", returnStdout: true).trim()
                        sh "echo ${ecrLogin} | docker login --username AWS --password-stdin 975050024946.dkr.ecr.eu-north-1.amazonaws.com"
                    }
                }
            }
        }
        stage('Push Docker Images to ECR') {
            steps {
                script {
                    // Push the first image
                    sh "docker tag ${IMAGE_NAME_1}:${GIT_COMMIT} 975050024946.dkr.ecr.eu-north-1.amazonaws.com/${ECR_REPOSITORY_1}:${GIT_COMMIT}"
                    sh "docker push 975050024946.dkr.ecr.eu-north-1.amazonaws.com/${ECR_REPOSITORY_1}:${GIT_COMMIT}"

                    // Push the second image
                    sh "docker tag ${IMAGE_NAME_2}:${GIT_COMMIT} 975050024946.dkr.ecr.eu-north-1.amazonaws.com/${ECR_REPOSITORY_2}:${GIT_COMMIT}"
                    sh "docker push 975050024946.dkr.ecr.eu-north-1.amazonaws.com/${ECR_REPOSITORY_2}:${GIT_COMMIT}"
                    
                    // Push the third image 
                    sh "docker tag ${IMAGE_NAME_3}:${GIT_COMMIT} 975050024946.dkr.ecr.eu-north-1.amazonaws.com/${ECR_REPOSITORY_3}:${GIT_COMMIT}"
                    sh "docker push 975050024946.dkr.ecr.eu-north-1.amazonaws.com/${ECR_REPOSITORY_3}:${GIT_COMMIT}"
                }
            }
        }
    }
    post {
        success {
            echo 'Docker images built and pushed successfully.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
