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
        MYVAR=credentials('SECKEY')
            
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
