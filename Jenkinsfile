#!/usr/bin/env groovy
def releases

node {
   checkout scm
   sh (script: "pwd", returnStdout: true).trim()
   sh (script: "ls", returnStdout: true).trim()
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
