from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        open_ = float(request.form['open'])
        high = float(request.form['high'])
        low = float(request.form['low'])

        features = np.array([[open_, high, low]])
        prediction = model.predict(features)[0]

        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
