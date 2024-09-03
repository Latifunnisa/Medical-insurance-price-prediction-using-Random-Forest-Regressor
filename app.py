import pickle
import pandas as pd
from flask import Flask, render_template, request

#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


# Load the trained model and scaler
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def preprocess_input(data):
    data_scaled = scaler.transform(data)
    return pd.DataFrame(data_scaled, columns=data.columns)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        # convert categorical data
        sex = 1 if sex == 'male' else 0
        smoker = 1 if smoker == 'yes' else 0
        region_map = {'southeast': 0, 'southwest': 1, 'northwest': 2, 'northeast': 3}
        region = region_map[region]

        # create dataframe for input data
        input_data = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker],
            'region': [region]
        })

        input_data_processed = preprocess_input(input_data)
        prediction = rf_model.predict(input_data_processed)
        return render_template("result.html",
                               prediction=f'Predicted Insurance Cost: ${prediction[0]:.2f}')


if __name__ == '__main__':
    app.run(debug=True)
