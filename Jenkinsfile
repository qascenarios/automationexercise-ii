
pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
        DOCKER_IMAGE = 'topdandy/automationexercise-ii-mb'
        IMAGE_TAG = 'latest'
        ALLURE_RESULTS = 'allure-results'
    }

    stages {

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKERHUB_CREDENTIALS,
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$IMAGE_TAG .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh 'docker push $DOCKER_IMAGE:$IMAGE_TAG'
            }
        }

        stage('Clean Previous Allure Results') {
            steps {
                sh '''
                    rm -rf $ALLURE_RESULTS
                    mkdir -p $ALLURE_RESULTS
                '''
            }
        }

        stage('Run Playwright Tests in Docker') {
            steps {
                sh '''
                    docker run --rm \
                      -v $(pwd)/$ALLURE_RESULTS:/app/$ALLURE_RESULTS \
                      $DOCKER_IMAGE:$IMAGE_TAG \
                      pytest tests --alluredir=/app/$ALLURE_RESULTS
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: "$ALLURE_RESULTS"]]
            }
        }
    }

    post {
        always {
            sh 'docker logout'
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed. Check logs and Allure report.'
        }
    }
}
