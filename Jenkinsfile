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
                    export ACCKEY="key001"
                    export SECKEY="sec001"
                    export MYVAR="var001"
                    python myscript.py
                   '''    
            }
        }
    }
}
