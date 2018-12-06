#!/usr/bin/env groovy
def releases

node {
   sh (script: "echo ${PWD}", returnStdout: true).trim()
   releases = sh (script: "${PWD}@script/_scripts/get_releases.py", returnStdout: true).trim()
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
