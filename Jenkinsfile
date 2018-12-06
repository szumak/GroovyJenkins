#!/usr/bin/env groovy
/* source: https://github.com/jenkins-infra/jenkins.io/blob/master/Jenkinsfile/ */

try {
   node('any') {
      stage('Start') {
         sh 'echo start'
      }
   }
}
catch (exc) {
    echo "Caught: ${exc}"
    throw exc
}
