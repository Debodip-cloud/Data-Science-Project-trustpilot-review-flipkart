# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:07:16 2025

@author: Debodip Chowdhury
"""
from flask import Flask, request, jsonify
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load artifacts
model = load_model('C:/Users/Debodip Chowdhury/Downloads/flipkart_sentiment_model.keras')
with open('C:/Users/Debodip Chowdhury/Downloads/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('C:/Users/Debodip Chowdhury/Downloads/label_encoder.pkl', 'rb') as handle:
    le = pickle.load(handle)

MAX_LEN = 100  # Same as during training

# POST method
@app.route('/predict', methods=['POST'])
def predict_post():
    try:
        # Get review text from POST request
        data = request.get_json()
        text = data['text']

        # Preprocess
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=MAX_LEN)

        # Predict
        pred = model.predict(padded)
        sentiment = le.inverse_transform([np.argmax(pred)])[0]
        confidence = float(np.max(pred))

        return jsonify({
            'sentiment': sentiment,
            'confidence': confidence,
            'text': text
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# GET method
@app.route('/predict', methods=['GET'])
def predict_get():
    try:
        # Get review text from GET request (query parameter)
        text = request.args.get('text')

        if not text:
            return jsonify({'error': 'No text parameter provided'}), 400

        # Preprocess
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=MAX_LEN)

        # Predict
        pred = model.predict(padded)
        sentiment = le.inverse_transform([np.argmax(pred)])[0]
        confidence = float(np.max(pred))

        return jsonify({
            'sentiment': sentiment,
            'confidence': confidence,
            'text': text
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    import sys
    sys.argv = ['']  # Prevent SystemExit in Spyder
    app.run(debug=True, use_reloader=False)  # Stops the reloader
