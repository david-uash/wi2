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
#                withCredentials([gitUsernamePassword(credentialsId: 'my-credentials-id', gitToolName: 'git-tool')]) {
                sh '''
                    python myscript.py
                   '''    
#                }
            }
        }
    }
}
