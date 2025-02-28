pipeline {
    agent any

    environment {
        // Set up Python environment
        VIRTUALENV_DIR = '.venv'
        PYTHON = 'python3'  // You can adjust this if you use a different Python version or environment
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub repository
                git branch: 'master', url: 'https://github.com/jayeshkurella/python-server.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Create a virtual environment if it doesn't exist
                    sh 'python3 -m venv ${VIRTUALENV_DIR}'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies using pip from requirements.txt
                    sh './${VIRTUALENV_DIR}/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    sh './${VIRTUALENV_DIR}/bin/python -m pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Example: Deploy your Python app (modify with your specific deployment steps)
                    // You can replace this with your actual deploy command or script
                    echo 'Deploying the application...'
                    sh './${VIRTUALENV_DIR}/bin/python deploy.py' // Replace with your deploy command
                }
            }
        }
    }

    post {
        always {
            // Cleanup virtual environment after deployment
            echo 'Cleaning up...'
            sh 'rm -rf ${VIRTUALENV_DIR}'
        }

        success {
            echo 'Build and Deployment Successful!'
        }

        failure {
            echo 'Build or Deployment Failed!'
        }
    }
}
