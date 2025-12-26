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
       sh 'docker build --no-cache -t ${IMAGE_NAME}:latest .'
      }
    }

    // --- NEW STAGE ADDED HERE ---
  stage('Test') {
    steps {
        sh '''
        pip install pytest pytest-xml-reporting
        pytest
        '''
    }
}

    // ----------------------------
    
    stage('Push to Dockerhub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
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
