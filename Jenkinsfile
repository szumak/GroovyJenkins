#!/usr/bin/env groovy
def releases
def versions
def options
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
          applications = sh (script: "./_scripts/get_releases.py -c config.ini -r ${chosen_release}", returnStdout: true).trim().split('\n')
          def choice_app = [];
          applications.each {
            jenkinsJobName = sh (script: "./_scripts/get_releases.py -c config.ini -a ${it}", returnStdout: true).trim()
            options = getBuilds(jenkinsJobName)
            choice_app.push( choice( name: "${it}", choices: "${options}", description:'' ) )
          }
          versions = input message: 'Choose testload version!', ok: 'SET', parameters: choice_app 
        }
      }
    }

    stage("build") {
      steps {
        script {
          def myOpt = [];
          versions.each { 
            myOpt.push( "${it.key}${it.value}" )
          } 
          options = "-ab " + myOpt.join(",")
          println "OPTIONS: " + options
        }
      }
    }
   
  }
}


// FUNCTIONS
@NonCPS
def getBuilds(name) {
  def item = Jenkins.instance.getItemByFullName(name)
  tmp_options = []
  item.builds.each {
    tmp_options.push( "#" + it.getNumber() ) 
  }
  return tmp_options.take(5).join("\n")
}
