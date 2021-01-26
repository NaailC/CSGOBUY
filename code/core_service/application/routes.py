from application import app, db
from flask import Flask, redirect, url_for, render_template
from sqlalchemy import desc
import requests
from requests import get
from os import getenv
from random import choice

class Buy(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    weapon = db.Column(db.String(20), nullable=False)
    strat = db.Column(db.String(50), nullable=False)
    power = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    weapon_response = requests.get('http://CSGOBG-stack_buy_backend:5001/get/buy')
    buystrength_response = requests.post('http://CSGOBG-stack_buy_backend:5001/post/buystrength', data=weapon_response.text)
    strat_response = requests.get('http://CSGOBG-stack_strat_backend:5002/get/strat')
    stratstrength_response = requests.post('http://CSGOBG-stack_strat_backend:5002/post/stratstrength', data=strat_response.text)
    roundstrength_response = requests.post('http://CSGOBG-stack_round_strength:5003/post/roundstrength', json={'buystrength' : buystrength_response.text, 'stratstrength' : stratstrength_response.text})

    db.session.add(Buy(
        weapon = weapon_response.text, 
        strat = strat_response.text,
        power = roundstrength_response.text
    ))
    db.session.commit()

    show = Buy.query.order_by(desc("id")).limit(5).all()

    gif = random.choice['HandmadeDiscreteEasternnewt',
        'veneratedcomposedgrassspider',
        'shorttermscentedjaeger',
        'wandangerousirukandjijellyfish',
        'discretegraciousgallowaycow',
        'maleregularlangur',
        'drearyimpurearmyworm',
        'criminalvengefulkatydid',
        'occasionalclearcutjellyfish']
    
    return render_template('home.html', weapon=weapon_response.text, strat=strat_response.text, roundstrength=roundstrength_response.text, show=show, gif=gif)



