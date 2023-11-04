pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
    }

    stages {
        stage('Set Global Bucket Names') {
            steps {
                script {
                    def BUCKET_NAMES = ['test-input-bucket', 'test-output-bucket']
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
                        try {
                            sh "aws s3api head-bucket --bucket $bucketName --region $AWS_REGION"
                            echo "Bucket '$bucketName' exists."
                        } catch (Exception e) {
                            echo "Bucket '$bucketName' doesn't exist. Creating..."
                            sh "aws s3api create-bucket --bucket $bucketName --region $AWS_REGION --create-bucket-configuration LocationConstraint=EU"
                        }
                    }
                }
            }
        }
    }
}

