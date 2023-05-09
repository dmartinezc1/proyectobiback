from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import modelo1

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=['POST'])
def predict():
    review = request.json['review']

    sentiment = modelo1.predict([review])
    print(sentiment[0])
    if sentiment[0]==1:
        return jsonify({'sentiment': 'Positivo'})
    return jsonify({'sentiment': 'Negativo'})
