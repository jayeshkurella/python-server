pipeline {
    agent any

    environment {
        // Set up Python environment
        VIRTUALENV_DIR = '.venv'
        PYTHON = 'python3'  // Adjust this if you use a different Python version or environment
        SERVER_PORT = '9090' // Port for the Django server
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
                    echo 'Setting up Python virtual environment...'
                    sh 'python3 -m venv ${VIRTUALENV_DIR}'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies using pip from requirements.txt
                    echo 'Installing dependencies...'
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
                    sh 'nohup ./${VIRTUALENV_DIR}/bin/python manage.py runserver 0.0.0.0:${SERVER_PORT} &'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                // Ensure the application is stopped first
                echo 'Stopping any running server processes...'
                sh """
                    kill \$(lsof -t -i:${SERVER_PORT}) || true
                """

                // Ensure proper permissions to remove .venv
                echo 'Adjusting permissions on .venv directory...'
                sh """
                    sudo chown -R \$(whoami):\$(whoami) ${VIRTUALENV_DIR}
                    sudo chmod -R 777 ${VIRTUALENV_DIR}
                """

                // Retry logic to clean up .venv directory in case of failures
                echo 'Attempting to clean up the virtual environment...'
                for i in {1..5}; do
                    rm -rf ${VIRTUALENV_DIR} && break || sleep 2
                done

                // Verify if .venv was removed
                if (fileExists(VIRTUALENV_DIR)) {
                    echo "Failed to delete ${VIRTUALENV_DIR} directory."
                } else {
                    echo "${VIRTUALENV_DIR} directory successfully deleted."
                }
            }
        }

        success {
            echo 'Build and Deployment Successful!'
            // Print the URL to access the app
            echo "You can access the app at: http://172.20.67.173:${SERVER_PORT}"
        }

        failure {
            echo 'Build or Deployment Failed!'
        }
    }
}
