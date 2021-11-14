pipeline {
    agent { docker 
           { 
               image 'python'
               args '-u root -v /tmp/python:/mnt/secret/'
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
