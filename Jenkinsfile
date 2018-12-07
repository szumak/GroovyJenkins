#!/usr/bin/env groovy
def releases
import jenkins.model.Jenkins

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
          applications = sh (script: "./_scripts/get_releases.py -c config.ini -r ${chosen_release}", returnStdout: true).trim().split('\n')
          def choice_app = [];
          applications.each {
            println "Application ${it}"     
            choice_app.push( choice( name: "${it}", choices: "${version_collection}", description:'' ) )
          }
          versions = input message: 'Choose testload version!', ok: 'SET', parameters: choice_app 
        }
      }
    }

    stage("build") {
      steps {
        script {
          echo "Selected release: ${params.Release}"
          Jenkins.instance.getAllItems().each {
            println(it.fullName)
          };
		jenkins.model.Jenkins.instance?.getAllItems().each { folder ->
		  println "Folder - ${folder}"
	           folder.getItems().each {
		     println "\t job - ${it}"
		   } 
		} 
        }
      }
    }
   
  }
}
