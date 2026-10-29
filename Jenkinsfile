
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        
        stage('Check Docker') {
            steps {
                bat '"C:\\Users\\mdnik\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" version'
                bat '"C:\\Users\\mdnik\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" compose version'
            }
        }


        stage('Build Docker Image') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'docker compose up -d --force-recreate'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'docker compose ps'
                bat 'curl.exe -f http://localhost:5000/health'
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Deployment failed. Check Console Output.'
        }
    }
}
