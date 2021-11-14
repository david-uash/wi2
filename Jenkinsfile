pipeline {
    agent { docker { image 'python' } }
    stages {
        stage('build') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install numpy
                    python myscript.py
                   '''    
            }
        }
    }
}
