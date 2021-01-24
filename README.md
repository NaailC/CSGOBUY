# CSGOBUY

Brief

The DevOps Practical project is designed to fully test and showcase my knowledge from the first half of the DevOps course as well as to showcase my ability to operate as a junior/dev-ops engineer. This project focuses more on the CI pipeline than the complexity of the code.

Requirements

The Minumum Viable Product for this project is a fully complete CI/CD pipeline, integrated into a complete version control system utilising the feature/branch model. The application must be built wiht a microstructure architechture, with atleast 4 services being implemented. These are:

    Service 1: Connect all services persisting data in an SQL database
    Service 2+3: Generate a "random" object 
    Service 4: Generate an object that is built based on the objects generated previously

Scope

    An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
    An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
    If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
    The project must follow the Service-oriented architecture that has been asked for.
    The project must be deployed using containerisation and an orchestration tool.
    As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
    The project must make use of a reverse proxy to make your application accessible to the user.

Platform Specific

    Kanban Board: Jira
    Version Control: Git
    CI Server: Jenkins
    Configuration Management: Ansible
    Cloud server: GCP virtual machines
    Containerisation: Docker
    Orchestration Tool: Docker Swarm
    Reverse Proxy: NGINX

Chosen Idea: Counter Strike Buy Generator 

On refreshing the page the user is shown a new buy:

Service 1: Page which connects all the services in a HTML file and saves buys into a database

Service 2: Generates a random day weapon, and a buy strength for that weapon.

Service 3 : Generates a strategy, and a strength for a the strategy.

Service 4 : Generates a round strenght based on buy and stragegy.
