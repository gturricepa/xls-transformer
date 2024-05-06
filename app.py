from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def home():

    return 'server is running', 200


@app.route('/getuser', methods=['POST'])
def return_user():

    return jsonify({"data": "data here"}), 200

app.run(port=5000, host='localhost', debug=True)