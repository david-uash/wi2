pipeline {
    agent { docker { image 'python' } }
    stages {
        stage('build') {
            steps {
                sh '''
                    pip install numpy
                    python myscript.py
                   '''    
            }
        }
    }
}
