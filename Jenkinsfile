pipeline {
    agent any

    stages {
        stage('Set Up Python Environment') {
            steps {
              sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip && pip install streamlit'
            }
        }

  
        
    }
}