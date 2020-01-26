from flask import Flask, request, abort, jsonify

from lighting.lights import Lights
from lighting.colors import Colors, ColorSets


# Flask App
app = Flask(__name__)

l = Lights(240)
print(l)


@app.route("/", methods=["GET"])
def index():
    return "Up and Running!!!"


@app.route("/lights/state/", methods=["POST", "GET"])
def lights_state():
    return jsonify({"state": l.state}), 200


@app.route("/lights/fill/", methods=["POST",])
def lights_fill():
    data = request.json
    if not data:
        return "{}", 400
    try:
        color = data["color"]
        _scale = data["scale"]
        _range = data["range"]
        l.fill(color, _scale=_scale, _range=_range)
        return jsonify({'color': color, 'scale': _scale, 'range': _range}), 200
    except Exception as e:
        print(e)
        return "{}", 400


@app.route("/lights/off/", methods=["GET",])
def lights_off():
    l.clear()
    return "{}", 200


if __name__ == "__main__":
    app.debug == True
    app.run(host="0.0.0.0", port=5000, threaded=False) # threaded=False is important because Lights are set as a global variable
