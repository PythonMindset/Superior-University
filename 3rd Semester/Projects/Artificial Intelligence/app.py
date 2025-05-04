from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load all three models
with open('linear_model.pkl', 'rb') as f:
    linear_model = pickle.load(f)
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)
with open('svr_model.pkl', 'rb') as f:
    svr_model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect data from form
        data = [
            float(request.form['km_driven']),
            int(request.form['fuel']),
            int(request.form['seller_type']),
            int(request.form['transmission']),
            int(request.form['owner']),
            float(request.form['mileage']),
            float(request.form['engine']),
            float(request.form['max_power']),
            float(request.form['seats']),
            2025 - int(request.form['year'])  # Convert year to car_age
        ]

        final_input = np.array(data).reshape(1, -1)

        # Predict using all 3 models
        linear_pred = linear_model.predict(final_input)[0]
        rf_pred = rf_model.predict(final_input)[0]
        svr_pred = svr_model.predict(final_input)[0]

        return render_template('result.html',
                               linear_pred=round(linear_pred, 2),
                               rf_pred=round(rf_pred, 2),
                               svr_pred=round(svr_pred, 2))
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
