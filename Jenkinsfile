#!/usr/bin/env groovy
def releases

node {
   releases = sh (script: "../${JOB_NAME}@script/_scripts/get_releases.py", returnStdout: true).trim()
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
  }
}
