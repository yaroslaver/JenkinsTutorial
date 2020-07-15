
pipeline {
    // agent { docker { image 'manycoding/robotframework' } }
    agent { docker {
                image 'ppodgorsek/robot-framework:latest'
                args '--shm-size=1g -u root' }
            }

    stages {
        stage('start') {
            steps {
                sh 'python main.py'
            }
        }

        stage('test') {
            steps {
                sh 'robot robot/test.robot'
            }
        }
    }

    post {
        always {
            archive (includes: 'robot/*.html')
        }
    }
}
