from core_service import app 
from flask import Flask, request, jsonify
from buy_backend import app
from strat_backend import routes

@app.route('/roundstrength', methods=['GET'])
def get_roundstrength():
    weaponstrength = 
    roundstrength = 1
    return ((weaponstrength + roundstrength)/2)
# Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5003)