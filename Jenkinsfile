pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '''
                py --version
                py -m pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                py -m pip install --upgrade pip
                py -m pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                bat '''
                py src\\train_sklearn.py
                '''
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'models/*.pkl', fingerprint: true
            }
        }

    }
}
