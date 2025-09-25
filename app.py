from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/gutendex')
def gutendex_proxy():
    try:
        response = requests.get(
            'https://gutendex.com/books',
            params=request.args,
            timeout=10  # tempo máximo de espera em segundos
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
