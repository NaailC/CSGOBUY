from flask import request, Flask, jsonify, Response
import random

app = Flask(__name__)

@app.route('/get/buy', methods=['GET'])
def get_buy():
    x = ['Deagle', 
    'Dualies', 
    'Negev', 
    '57', 
    'Scout', 
    'Mac10', 
    'MP5',
    'UMP-45',
    'p250']
    return Response(str(random.choice(x)), mimetype='text/plain')

@app.route('/post/buystrength', methods=['POST'])
def get_buystrength():
    buystrength = {'Deagle' : 100,
                'Dualies' : 20, 
                'Negev' : 75, 
                '57' : 50, 
                'Scout' : 55,  
                'Mac10' : 30, 
                'MP5' : 45,
                'UMP-45' : 35,
                'p250' : 45}
    x = request.data.decode('utf-8')
    return Response(str(buystrength[x]), mimetype='text/plain')

# Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5001)