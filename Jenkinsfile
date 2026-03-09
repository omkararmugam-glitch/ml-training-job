pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                bat '''
                python src\\train_sklearn.py
                '''
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'models/*', fingerprint: true
            }
        }
    }
}
