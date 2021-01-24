#!/bin/bash
scp -i ~/jenkins_agent_key docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
ssh -i ~/jenkins_agent_key jenkins@swarm-master << EOF
    export DATABASE_URI=${DATABASE_URI} 
    export app_version=${app_version} 
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml CSGOBG-stack
EOF