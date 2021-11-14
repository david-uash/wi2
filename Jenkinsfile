pipeline {
    agent { docker { image 'python' } }
    stages {
        stage('build') {
            steps {
                sh '''
                    /usr/local/bin/pip3 install numpy
                    python myscript.py
                   '''    
            }
        }
    }
}
