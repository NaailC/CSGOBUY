from core_service import app 
from flask import Flask, request, jsonify
from buy_backend import app
from strat_backend import routes

@app.route('/roundstrength', methods=['GET'])
def get_roundstrength():
    data = request.get_json()
    roundstrength = ((data['buystrength'].values() + data['stratstrength'].values()) /2)
    return str(roundstrength+'%')
# Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5003)