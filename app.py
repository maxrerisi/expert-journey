from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = []


@app.route("/data", methods=["POST"])
def receive_data():
    payload = request.get_json(force=True)  # parse JSON body
    value = payload.get("value")
    data_store.append(value)
    return jsonify(status="ok", received=value), 200


@app.route("/data", methods=["GET"])
def get_data():
    return {"values": data_store}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234, debug=True)
