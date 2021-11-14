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
                    ./mymodules.sh
                    python myscript.py
                   '''    
            }
        }
    }
}
