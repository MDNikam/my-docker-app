
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        bat "\"${scannerHome}\\bin\\sonar-scanner.bat\""
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 15, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                dependencyCheck(
                    odcInstallation: 'DP-Check',
                    additionalArguments: '--scan . --format XML --format HTML --out dependency-check-report --enableExperimental'
                )

                dependencyCheckPublisher(
                    pattern: 'dependency-check-report.xml'
                )
            }
        }

        stage('Check Docker and Trivy') {
            steps {
                bat '"C:\\Users\\mdnik\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" version'

                bat '"C:\\Users\\mdnik\\.docker\\cli-plugins\\docker-compose.exe" version'

                bat '"C:\\Trivy\\trivy.exe" --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\mdnik\\.docker\\cli-plugins\\docker-compose.exe" build'
            }
        }

        stage('Trivy Security Scan') {
            steps {
                // Report HIGH and CRITICAL vulnerabilities
                bat '"C:\\Trivy\\trivy.exe" image --scanners vuln --severity HIGH,CRITICAL my-docker-app-pipeline-web:latest'

                // Block deployment if CRITICAL vulnerabilities exist
                bat '"C:\\Trivy\\trivy.exe" image --scanners vuln --severity CRITICAL --exit-code 1 my-docker-app-pipeline-web:latest'
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

                bat 'curl.exe -f http://127.0.0.1:5000/health'
            }
        }
    }

    post {
        success {
            echo 'Build, security scan and deployment successful!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
