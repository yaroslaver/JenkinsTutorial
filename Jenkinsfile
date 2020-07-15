
pipeline {
    agent { docker { image 'manycoding/robotframework' } }
    stages {
        stage('start') {
            steps {
                sh 'python main.py'
            }

        }
    }
}
