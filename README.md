# CSGOBUYGENERATOR

## Brief

The DevOps Practical project is designed to fully test and showcase my knowledge from the first half of the DevOps course as well as to showcase my ability to operate as a junior/dev-ops engineer. This project focuses more on the CI pipeline than the complexity of the code.

## Requirements

The Minumum Viable Product for this project is a fully complete CI/CD pipeline, integrated into a complete version control system utilising the feature/branch model. The application must be built wiht a microstructure architechture, with atleast 4 services being implemented. These are:

    Service 1: Connect all services persisting data in an SQL database
    Service 2+3: Generate a "random" object 
    Service 4: Generate an object that is built based on the objects generated previously

## Scope

* A Kanban board.
* An Application fully integrated using the Feature-Branch model into a Version Control System, built through a CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
* The app must follow a micro-service architecture.
* The project must be deployed using containerisation and an orchestration tool.
* Create an Ansible Playbook to deploy environments.
* The project must make use of a reverse proxy to make your application accessible to the user.

Platform Specific

    Kanban Board: Jira - easy to track tasks
    Version Control: Git - open source, easy to use
    CI Server: Jenkins - Capable of all the tasks needed for automation
    Configuration Management: Ansible - allows configuration of environments to be scripted
    Cloud server: GCP virtual machines - free, easy to connect
    Containerisation: Docker - open source, easy to use
    Orchestration Tool: Docker Swarm - works well with docker to stack images and deploy
    Reverse Proxy: NGINX - works well as a load balancer&reverse proxy

## Chosen Idea: Counter Strike Buy Generator 

On refreshing the page the user is shown a new buy:

Service 1: Page which connects all the services in a HTML file and saves buys into a database

Service 2: Generates a random weapon, and a buy strength for that weapon.

Service 3 : Generates a strategy, and a strength for a the strategy.

Service 4 : Generates a round strength based on buy and strategy.

A second implementation has generated an eco-buy and CT strategy

## Database ED

## CI Pipeline

The main goal of this project was to create a robust CI pipeline system, capabale of performing rolling updates with little to no downtime. As such, scripting methods were used with jenkins order to test, build and deploy the app. As versions are pushed onto the main hub of my github repository, a webhook automatically triggers, and imports the build to my jenkins server. 

## Testing

There were issues with testing my core-service. Due to the way I designed my apps, there was more than one route operating within each microservice, which made it difficult when using mock tests. 

