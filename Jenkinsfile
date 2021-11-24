pipeline {
    agent { docker 
           { 
               image 'python:aws'
               args '-u root' 
           } 
          }
    environment {
        ACCKEY=credentials('ACCKEY')
        SECKEY=credentials('SECKEY')
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
