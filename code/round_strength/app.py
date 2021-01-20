from core_service import app 
from flask import Flask, request, jsonify
from buy_backend import app
from strat_backend import routes

@app.route('/roundstrength', methods=['POST'])
def get_roundstrength():
    data = request.json()
    weapon = data['buystrength']
    strat = data['stratstrength']
    roundstrength = ((weapon.values() + strat.values()) /2)
    return str('your round power is', roundstrength, '%')

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5003)