from joblib import load

model = load('assets/modelo_iris.joblib')
species = ['setosa', 'versicolor', 'virginica']

if __name__ == '__main__':
    # Specify sample data
    sample_flower = [5.2, 2.7, 3.9, 1.4]

    # Predict using model
    prediction = model.predict([sample_flower])[0]
    print("Class prediction:", prediction)
    print("Species prediction:", species[prediction])
