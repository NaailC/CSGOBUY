from flask import Flask, request, jsonify, Response
import random

app = Flask(__name__)

timea = random.randint(20,105)
timeb = random.randint(20,105)

@app.route('/get/strat', methods=['GET'])
def get_tstrat():
    
    strat = ['Stack A',
        'Stack B',
        '4A',
        '4B',
        'Default']
    choice = random.choice(strat)
    if choice == timea:
        return Response(f'Push A at {timea} seconds', mimetype='plain/text')
    elif choice == timeb:
        return Response(f'Push B at {timeb} seconds', mimetype='plain/text')
    else:
        return Response(f'{choice}', mimetype='plain/text')

@app.route('/post/stratstrength', methods=['POST'])
def get_tstratstrength():
    choice = request.data.decode('utf-8')
    stratstrength = {'Stack A' : 30,
        'Stack B' : 40,
        '4A' : 60,
        '4B' : 50,
        'Default' : 90}
    return Response(str(stratstrength[choice]), mimetype='plain/text')
    # Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5002)