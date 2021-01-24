#!/bin/bash
scp -i ~/.ssh/swarmid docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/swarmid jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI} replicas=${replicas}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml CSGOBG-stack
EOF