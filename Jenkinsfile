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

          def name = "myJenkinsPipeline/github-groovyJenkins"
          def item = Jenkins.instance.getItemByFullName(name)
          options = []
          item.builds.each {
            options.push( "#" + it.getNumber() ) 
          }
          options = options.take(10).join("\n")
          println "OPTIONS: " + options
          applications = sh (script: "./_scripts/get_releases.py -c config.ini -r ${params.Release}", returnStdout: true).trim().split('\n')
          def choice_app = [];
          applications.each {
            println "Application ${it}"     
            choice_app.push( choice( name: "${it}", choices: "${releases}", description:'' ) )
          }
          versions = input message: 'Choose testload version!', ok: 'SET', parameters: choice_app 
        }
      }
    }

    stage("build") {
      steps {
        script {
          println "Selected release: ${params.Release}"
          //println "Selected version: ${params.}"
          
        }
      }
    }
   
  }
}
