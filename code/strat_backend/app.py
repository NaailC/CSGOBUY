from flask import Flask, request, jsonify, Response
import random

app = Flask(__name__)


@app.route('/get/strat', methods=['GET'])
def get_tstrat():
    
    timea = random.randint(20,105)
    timeb = random.randint(20,106)
    strat = ['Rush A',
        'Rush B',
        timea,
        timeb]
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
    stgen = random.randint(35,75)
    stratstrength = {'Rush A' : 50, 
        'Rush B' : 60,
        f'Push A at {choice} seconds' : stgen,
        f'Push B at {choice} seconds' : stgen}
    return Response(str(stratstrength[choice]), mimetype='plain/text')
    # Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5002)