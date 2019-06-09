from flask import Flask, jsonify, request
from flask_cors import cross_origin
from werkzeug.exceptions import BadRequest
from model import predict
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
@cross_origin
def index():
    return jsonify({"status":"ok"})


@app.route("/predict", methods=["POST"])
@cross_origin
def predict_view():
    input_file = request.files.get('file')
    if not input_file:
        return BadRequest("File not present in request")
    input_file.save('temp.mp3')
    genre = predict("temp.mp3")
    os.remove('temp.mp3')
    return jsonify({'genre':genre})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)