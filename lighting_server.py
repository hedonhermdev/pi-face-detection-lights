from flask import Flask, request, abort, jsonify
from flask import g

from lighting.lights import Lights
from lighting.colors import Colors, ColorSets


# Flask App
app = Flask(__name__)

l = Lights(240)
print(l)

@app.route('/lights/state/', methods=['POST','GET'])
def lights_state():
    return jsonify({'state': l.state}), 200


@app.route('/lights/fill/', methods=['POST',])
def lights_fill():
    print(request.json)
    data = request.json
    print(data)
    if not data:
        return "{}", 400
    try:
        l.fill(data['color'])
        return "{}", 200
    except Exception as e:
        print(e)
        return "{}", 400

@app.route('/lights/off/', methods=['GET',])
def lights_off():
    l.clear()
    return "{}", 200


if __name__ == "__main__":
    app.debug == True
    app.run(host='10.3.141.1', port=5000, threaded=False)
