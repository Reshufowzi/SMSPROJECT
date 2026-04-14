pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/your-repo/SMSPROJECT.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-app ./SMSPROJECT/studentproject'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop django-container || true
                docker rm django-container || true
                docker run -d -p 8000:8000 --name django-container django-app
                '''
            }
        }
    }
}
