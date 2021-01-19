from application import app
from flask import Flask, request, jsonify
import random

@app.route('/get/strat', methods=['GET'])
def get_tstrat():
    timea = random.randint(20,105)
    timeb = random.randint(20,105)
    strat = ['Rush A',
        'Rush B',
        timea,
        timeb]

    choice = random.choice(strat)
    if choice == timea:
        return str('Push A at', timea, 'seconds')
    elif choice == timeb:
        return str('Push B at', timeb, 'seconds')
    else:
        return choice 

@app.route('/get/stratstrength', methods=['GET'])
def get_tstratstrength():
    choice = request.data.decode('utf-8')
    stratstrength = {'Rush A' : 50, 
        'Rush B' : 60,
        timea : 80,
        timeb : 70}
    return jsonify(stratstrength[choice], mimetype='plain/text')