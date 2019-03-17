pipeline {
  agent any 
  options {
    timestamps()
  }
  stages {
    stage("Build docker image") {
      agent {
        node {
            label 'docker'
        }
      }
      environment {
        registry = "liamnou/main"
      }
      steps {
        script {
          docker.withRegistry("https://registry.hub.docker.com", "docker-id-password") {
            def customImage = docker.build registry + ":$BUILD_NUMBER"
            customImage.push()
          }
        }
      }
    }
    stage("Deploy image into k8s") {
      environment {
        releaseName = "its"
        appName = "test-task"
        fullName = "$releaseName-$appName"
      }
      steps {
        script {
          try {
            echo "Performing cleanup..."
            bat "helm del --purge $releaseName"
          }
          catch (error) {
            echo "Failed to delete release $releaseName"
          }
        }
        echo "Starting deployment..."
        bat "helm install ./.kube/$appName --name $releaseName && kubectl rollout status --watch deployment/$fullName"
      }
    }
  }
}