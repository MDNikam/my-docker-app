```groovy
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
                bat '"C:\\Users\\mdnik\\.docker\\cli-plugins\\docker-compose.exe" version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\mdnik\\.docker\\cli-plugins\\docker-compose.exe" build'
            }
        }

        stage('Deploy Application') {
            steps {
                bat '"C:\\Users\\mdnik\\.docker\\cli-plugins\\docker-compose.exe" up -d --force-recreate'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat '"C:\\Users\\mdnik\\.docker\\cli-plugins\\docker-compose.exe" ps'
                bat 'curl.exe -f http://localhost:5000/health'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed. Check Console Output.'
        }
    }
}
```
