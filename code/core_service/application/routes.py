from application import app
from flask import Flask, redirect, url_for, render_template
import requests
from requests import get


@app.route('/', methods=['GET', 'POST'])
def home():
    weapon_response = requests.get('http://CSGO-code-buy_backend:5001/get/buy')
    strat_response = requests.get('http://CSGO-code-strat_backend:5002/get/strat')
    roundstrength_response = requests.post('http://CSGO-code-round_strength:5003/post', json={'buystrength' : weapon_response.json['x'], 'stratstrength' : strat_response.json['strat']}
    return render_template('home.html', weapon=weapon_response.text, strat=strat_response.text, roundstrength=roundstrength_response.text)



