from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route('/post/roundstrength', methods=['POST'])
def get_roundstrength():
    data = request.json
    weapon = data['buystrength']
    strat = data['stratstrength']
    roundstrength = ((int(weapon) + int(strat)) /2)
    return Response(str(roundstrength), mimetype='plain/text')

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port=5003)