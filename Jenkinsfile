pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code already checked out by SCM'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Testing... (you can add pytest or unittest here)'
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Running Flask app'
                sh 'nohup python3 app.py &'
            }
        }
    }
}
