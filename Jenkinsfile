pipeline {
    agent { docker 
           { 
               image 'python'
               args '-u root'
           } 
          }
    stages {
        stage('build') {
            steps {
                sh '''
                    whoami
                    bash mymodules.sh
                    python myscript.py
                   '''    
            }
        }
    }
}
