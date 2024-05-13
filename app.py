from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def home():

    return 'Server is running', 200


@app.route('/getdata', methods=['POST'])
def return_xls():
    if 'xlsFile' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado.'}), 400
    
    xls_file = request.files['xlsFile']
    try:
        df = pd.read_excel(xls_file)
        print(df.head)
        return jsonify({'success': 'Arquivo XLS recebido e processado com sucesso.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(port=5000, host='0.0.0.0', debug=True)