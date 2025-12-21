pipeline {
    agent any

    environment {
        IMAGE_NAME = "topdandy/automationexercise-ii:latest"
        ALLURE_RESULTS = "allure-results"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Clean Previous Allure Results') {
            steps {
                echo 'Cleaning old Allure results...'
                sh "rm -rf ${ALLURE_RESULTS}"
                sh "mkdir -p ${ALLURE_RESULTS}"
            }
        }

        stage('Run Playwright Tests in Docker') {
            steps {
                echo 'Running tests inside Docker container...'
                sh """
                docker run --rm \
                  -v \$(pwd)/${ALLURE_RESULTS}:/app/${ALLURE_RESULTS} \
                  ${IMAGE_NAME}
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                echo 'Publishing Allure report...'
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }

        failure {
            echo 'Pipeline failed. Check test results and Allure report.'
        }
    }
}
