pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '''
                "C:\\Users\\omkar\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                "C:\\Users\\omkar\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install --upgrade pip
                "C:\\Users\\omkar\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                bat '''
                "C:\\Users\\omkar\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" src\\train_sklearn.py
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

