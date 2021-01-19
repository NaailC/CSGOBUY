from core_service import app 
from flask import Flask, request, jsonify
from buy_backend import routes
from strat_backend import routes

@app.route('/roundstrength', methods=['GET'])
def get_roundstrength():
    weaponstrength = 
    roundstrength = 
    return ((weaponstrength + roundstrength)/2)