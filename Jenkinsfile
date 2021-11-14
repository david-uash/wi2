pipeline {
    agent { docker { image 'python' } }
    stages {
        stage('build') {
            steps {
                sh 'python myscript.py'
            }
        }
    }
}
