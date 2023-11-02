pipeline {
    agent any

    stages {
        stage('AWS CLI Command') {
            steps {
                script {
                    sh 'aws s3 ls'  // Example AWS CLI command
                }
            }
        }

        stage('Docker CLI Command') {
            steps {
                script {
                    sh 'docker info'  // Example AWS CLI command
                }
            }
        }
    }
}
