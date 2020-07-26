pipeline {
    agent { dockerfile true }
    stages {
        stage('Build') {
            steps {
                sh 'sudo docker build -t csm-backend .'
            }
        }
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Run') {
            steps {
                sh 'sudo docker run --env-file .env-file -p 5000:5000 csm-backend'
            }
        }
    }
}