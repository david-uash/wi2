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
                    source mymodules.sh
                    python myscript.py
                   '''    
            }
        }
    }
}
