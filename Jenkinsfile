pipeline {
    agent any

    environment {
        BUCKET_NAMES = "['test-input-bucket', 'test-output-bucket']" // Add your bucket names to the list
        AWS_REGION = 'eu-north-1'
    }

    stages {
        stage('Check and Create S3 Buckets') {
            steps {
                script {
                    for (bucketName in BUCKET_NAMES) {
                        try {
                            sh """
                            aws s3api head-bucket --bucket $bucketName --region $AWS_REGION
                            """
                            echo 'Bucket ${bucketName} exists.'
                        } catch (Exception e) {
                            echo 'Bucket ${bucketName} doesn't exist. Creating...'
                            sh """
                            aws s3api create-bucket --bucket $bucketName --region $AWS_REGION
                            """
                        }
                    }
                }
            }
        }
    }
}
