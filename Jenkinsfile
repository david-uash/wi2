pipeline {
    agent { docker 
           { 
               image 'python:aws'
               args '-u root' 
           } 
          }
    environment {
        ACCKEY="key002"
        SECKEY="sec002"
        MYVAR="var002"
    }
    stages {
        stage('build') {
            steps {
                sh '''
                    python myscript.py
                   '''    
            }
        }
    }
}
