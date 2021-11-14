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
                    /usr/local/bin/pip3 install numpy --user
                    python myscript.py
                   '''    
            }
        }
    }
}
