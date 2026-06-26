from flask import Flask, request, jsonify, send_file
import requests

app = Flask(__name__)

API_URL = "https://api.exchangerate-api.com/v4/latest/"

@app.route('/')
def home():
    # Serve index.html directly from project root
    return send_file("index.html")

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json
    from_currency = data['from']
    to_currency = data['to']
    amount = float(data['amount'])

    response = requests.get(API_URL + from_currency)
    rates = response.json()['rates']

    if to_currency in rates:
        converted_amount = amount * rates[to_currency]
        return jsonify({'result': round(converted_amount, 2)})
    else:
        return jsonify({'error': 'Currency not supported'})

if __name__ == "__main__":
    app.run(debug=True)
