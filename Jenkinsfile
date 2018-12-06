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

    stage("stage 2") {
      steps {
        script {
          def chosen_release = "${params.Release}"
          version_collection = sh (script: "./_scripts/get_releases.py -c config.ini", returnStdout: true).trim()
          versions = input message: 'Choose testload version!', ok: 'SET', parameters: [ 
                                                                                         choice(name: 'APP1', choices: "${version_collection}", description: ''),
                                                                                         choice(name: 'APP2', choices: "${version_collection}", description: '')]
        }
      }
    }

    stage("build") {
      steps {
        script {
          echo "Selected release: ${params.Release}"
        }
      }
    }
   
  }
}
