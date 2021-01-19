from application import app
from flask import Flask, requests, redirect, url_for, render_template
from requests import get

ip = get('https://api.ipify.org/').text
url = 'http://'+ip

@app.route('/', methods=['GET'])
def home():
    weapon = generate_weapon()
    strat = generate_strat()
    return render_template('home.html', weapon=weapon, strat=strat)

@app.route('/buy')
def generate_weapon():
    response = requests.get(url+':5001/get/buy')
    return str(response.text)

@app.route('/strat')
def generate_strat():
    response = requests.get(url+':5002/get/strat')
    return str(response.text) 

