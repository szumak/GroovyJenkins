#!/usr/bin/env groovy
def releases

node {
   checkout scm
   releases = sh (script: "./_scripts/get_releases.py -c config.ini", returnStdout: true).trim()
}

pipeline {
  agent any

  parameters {
    choice(name: 'Release', choices:"${releases}", description: "")
  }

  stages {
    stage("stage 1") {
      steps {
         sh "echo start"
      }
    }
   
    stage("choose application build") {
      steps {
        script {
          def chosen_release = "${params.Release}"
          echo "you choice: $chosen_release"
        }
      }
    }
  }
}
