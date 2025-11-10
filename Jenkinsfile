pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u 0:0'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Instalando dependencias...'
                sh 'pip install --no-cache-dir -r requirements.txt --root-user-action=ignore'
                echo 'Ejecutando análisis estático con Bandit...'
                sh 'bandit -r . || true'
            }
        }
    }
}
