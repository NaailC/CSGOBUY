from application import app
from flask import Flask, redirect, url_for, render_template
import requests
from requests import get


@app.route('/', methods=['GET', 'POST'])
def home():
    weapon = requests.get('http://buy_backend:5001/get/buy')
    strat = requests.get('http://strat_backend:5002/get/strat')
    roundstrength = requests.post('http://round_strength:5003/post')
    return render_template('home.html', weapon=weapon, strat=strat)



