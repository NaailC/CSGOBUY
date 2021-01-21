from flask import Flask, request, jsonify
import random

app = Flask(__name__)

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
        return str(choice) 

@app.route('/post/stratstrength', methods=['POST'])
def get_tstratstrength():
    choice = request.data.decode('utf-8')
    stratstrength = {'Rush A' : 50, 
        'Rush B' : 60,
        timea : 80,
        timeb : 70}
    return Response(str(stratstrength[choice]), mimetype='text/plain')

    # Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5002)