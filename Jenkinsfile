pipeline {
  agent any
  
  environment {
    IMAGE_NAME = 'iamabi/test-flask'
  }
  
  stages {
    stage('Checkout git') {
      steps {
        git branch: 'main', url: 'https://github.com/Parth2k3/test-flask'
      }
    }
    
    stage('Build Docker Images') {
      steps {
        // Changed 'bat' to 'sh' and '%VAR%' to '${VAR}'
        sh 'docker build -t ${IMAGE_NAME}:latest .'
      }
    }
    
    stage('Push to Dockerhub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          // Changed 'bat' to 'sh' and adjusted variable syntax for shell
          sh """
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push ${IMAGE_NAME}:latest
            docker logout
          """
        }
      }
    }
  }
}
