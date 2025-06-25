from flask import Flask, request, render_template
import numpy as np
import pickle
import os

# Load trained model
MODEL_PATH = 'model/house_price_model.pkl'
model = pickle.load(open(MODEL_PATH, 'rb'))

# Initialize Flask app
app = Flask(__name__)  # Default folders: templates/ and static/

@app.route('/')
def home():
    return render_template('index.html')  # Show input form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs from form
        data = [float(request.form.get(f)) for f in [
            'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'
        ]]
        
        # Make prediction
        prediction = model.predict([data])[0]
        prediction = round(prediction, 2)

        # Show result in a new HTML page
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
