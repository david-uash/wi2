pipeline {
    agent { docker 
           { 
               image 'python:aws'
               args '-u root' 
           } 
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
