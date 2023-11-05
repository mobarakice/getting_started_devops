
def FUNC_NAMES = [
        'factory-lambda-test' : './apigateway_lambd_test',
        's3-trigger-function' : './factory_lamba_test',
        'apigateway-function' : './s3_bucket_trigger_test'
]

pipeline {
    agent any

    // Set necessary environment variable
    // Create S3 bucket if not exist
    // Create ECR repository if not exist
    // Build docker image
    // Login to ECR repository for uploading docker image
    // Create Image tag and upload Image into ECR repo
    // Create/Update lambda function with ECR Image URI and add s3 trigger
    // Update policy


    environment {
        AWS_REGION = 'eu-north-1'
        ECR_REPO_NAME = ""
    }

    stages {
        stage('Set Global Bucket Names') {
            steps {
                script {
                    def BUCKET_NAMES = ['input-files-y2023', 'output-files-y2023']
                    env.BUCKET_NAMES = BUCKET_NAMES.join(',') // Convert the list to a comma-separated string
                }
            }
        }

        stage('Check and Create S3 Buckets') {
            steps {
                script {
                    // Access BUCKET_NAMES as a global environment variable
                    def bucketNames = env.BUCKET_NAMES.split(',') // Convert the string back to a list
                    for (bucketName in bucketNames) {
                        if(bucketName == 'input-files-y2023'){
                            env.TRIGGER_BUCKET = bucketName
                        }
                        try {
                            sh "aws s3api head-bucket --bucket $bucketName --region $AWS_REGION"
                            echo "Bucket '$bucketName' exists."
                        } catch (Exception e) {
                            echo "Bucket '$bucketName' doesn't exist. Creating..."
                            sh "aws s3api create-bucket \
                            --bucket $bucketName \
                            --region $AWS_REGION \
                            --create-bucket-configuration LocationConstraint=$AWS_REGION"
                        }
                    }
                }
            }
        }

        stage('Create ECR Repository and save URL into environment') {
            steps {
                script {
                    try {
                        sh "aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region $AWS_REGION"
                         // Repo exists
                    } catch (Exception e) {
                        // Create the ECR repository
                        sh "aws ecr create-repository --repository-name $ECR_REPO_NAME --region $AWS_REGION"
                    }

                    // Get the ECR repository URI
                    def ecrRepoUri = sh(script: "aws ecr describe-repositories --repository-names $ECR_REPO_NAME --region $AWS_REGION --query 'repositories[0].repositoryUri' --output text", returnStdout: true).trim()

                    // Set the ECR repository URI as an environment variable
                    env.ECR_REPO_URI = ecrRepoUri
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Access FUNC_NAMES as a global environment variable
                    FUNC_NAMES.each { key, val ->
                        if(key == 's3-trigger-function'){
                            env.TRIGGER_FUN = funcName
                        }

                        sh "docker build -t $key $val"
                    }
                }
            }
        }

        stage('Login to AWS ECR') {
            steps {
                script {
                     sh "aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin ${env.ECR_REPO_URI}"
                }
            }

        }

        stage('Create Tag and Push Image to ECR') {
            steps {
                script {
                    // Access FUNC_NAMES as a global environment variable
                    FUNC_NAMES.each { key, val ->
                        if(key == 's3-trigger-function'){
                            env.TRIGGER_FUN = funcName
                        }

                        // Tag the image for ECR
                        sh "docker tag $key:latest $ECR_REPO_URL/$ECR_REPO_NAVE:$key"

                        // Push the image to ECR
                        sh "docker push $env.ECR_REPO_URL:$key"
                    }
                }
            }
        }
    }
}

