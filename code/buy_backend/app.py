from flask import request, Flask, jsonify, Response
import random

app = Flask(__name__)

@app.route('/get/buy', methods=['GET'])
def get_buy():
    x = ['AK', 
    'Galil', 
    'm249', 
    'AWP', 
    'p90', 
    'SG', 
    'Autosniper']
    return Response(str(random.choice(x)), mimetype='text/plain')

@app.route('/post/buystrength', methods=['POST'])
def get_buystrength():
    buystrength = {'AK' : 100,
        'Galil' : 75,
        'm249' : 20,
        'AWP' : 80,
        'p90' : 60,
        'SG' : 85,
        'Autosniper' : 50}
    x = request.data.decode('utf-8')
    return Response(str(buystrength[x]), mimetype='text/plain')

# Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5001)