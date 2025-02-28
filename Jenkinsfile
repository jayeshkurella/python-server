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

        stage('Deploy') {
            steps {
                script {
                    // Deploy the Django app in the background
                    echo 'Deploying the application...'
                    // Run Django with nohup and background execution
                    sh 'nohup ./${VIRTUALENV_DIR}/bin/python manage.py runserver 0.0.0.0:9090 &'
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
            // Print the URL to access the app
            echo "You can access the app at: http://172.20.67.173:9090"
        }

        failure {
            echo 'Build or Deployment Failed!'
        }
    }
}
