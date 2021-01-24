#!/bin/bash

apt-get update
apt-get install -y python3-venv python3-pip

cd code/core_service
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
cd ..


cd code/buy_backend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=app --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
cd ..

cd code/strat_backend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=app --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
cd ..

cd code/round_strength
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=app --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ~