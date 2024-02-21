from datetime import datetime
import os

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from joblib import load
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load model and classes
model = load('model.joblib')
species = ['setosa', 'versicolor', 'virginica']


# Set base route
@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def base_route():
    headers = {'Content-Type': 'application/json'}
    message = {
        'message': 'Hello World!',
        'timestmap': datetime.now(),
    }
    json_message = jsonify(message)

    return make_response(json_message, 200, headers)


@app.route('/api/predict', methods=['GET', 'POST'])
def predict():
    headers = {'Content-Type': 'application/json'}

    if request.method == 'GET':
        message = {
            'message': 'Hello World!', 
            'timestmap': datetime.now(),
        }
        json_message = jsonify(message)
        response = make_response(json_message, 200, headers)
        return response

    if request.method == 'POST':
        data = request.get_json()

        input_data = np.array([
            data['sepal_length'], data['sepal_width'], data['petal_length'],
            data['petal_width']
        ])

        prediction = model.predict([input_data])
        message = {
            'input_data': input_data.tolist(),
            'prediction': int(prediction[0]),
            'species': species[prediction[0]],
            'timestmap': datetime.now()
        }

        json_message = jsonify(message)
        response = make_response(json_message, 200, headers)
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
