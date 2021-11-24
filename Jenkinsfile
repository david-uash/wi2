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
        MYVAR=${env.BUILD_ID}
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
