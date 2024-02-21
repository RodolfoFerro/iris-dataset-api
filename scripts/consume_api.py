from pprint import pprint

import requests

species = ['setosa', 'versicolor', 'virginica']

if __name__ == '__main__':
    # Set API URL
    url = 'http://0.0.0.0:5000/api/predict'

    # Specify sample data
    input_data = {
        'sepal_length': 5.2,
        'sepal_width': 2.7,
        'petal_length': 3.9,
        'petal_width': 1.4
    }

    response = requests.post(url, json=input_data)

    # Print response
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else:
        print("Status code:", response.status_code)
        print(response.text)
