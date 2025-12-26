pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        IMAGE_NAME = 'iamabi/test-flask'
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Parth2k3/test-flask'
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:${TAG} .
                docker tag ${IMAGE_NAME}:${TAG} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                docker run --rm ${IMAGE_NAME}:latest pytest
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push ${IMAGE_NAME}:${TAG}
                    docker push ${IMAGE_NAME}:latest
                    docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
    }
}
