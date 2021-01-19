from application import app
from flask import request, Flask, jsonify
import random

app = Flask(__name__)

@app.route('/get/buy', methods=['GET'])
def get_buy():
    x = ['ak/m4', 
    'galil/famas', 
    'm249', 
    'AWP', 
    'p90', 
    'SSG/AUG', 
    'Autosniper']
    return Response(str(random.choice(x)), mimetype='text/plain')

@app.route('/get/buystrength', methods['GET'])
def get_buystrength():
    x = request.data.decode('utf-8')
    buystrength = {'ak/m4' : 100,
        'galil/famas' : 75,
        'm249' : 20,
        'AWP' : 80,
        'p90' : 60,
        'SG/AUG' : 85,
        'Autosniper' : 50}
    return jsonify(buystrength[x], mimetype='plain/text')

# Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5001)