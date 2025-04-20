from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import pickle
from xgboost import XGBClassifier

app = Flask(__name__, template_folder="template")

# Load the trained model
model = pickle.load(open("xgboostmodel.pkl", "rb"))
print("Model Loaded")

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        try:
            # Parse and extract all form data
            date = request.form["date"]
            day = float(pd.to_datetime(date, format="%Y-%m-%d").day)
            month = float(pd.to_datetime(date, format="%Y-%m-%d").month)

            minTemp = float(request.form["mintemp"])
            maxTemp = float(request.form["maxtemp"])
            rainfall = float(request.form["rainfall"])
            evaporation = float(request.form["evaporation"])
            sunshine = float(request.form["sunshine"])
            windGustSpeed = float(request.form["windgustspeed"])
            windSpeed9am = float(request.form["windspeed9am"])
            windSpeed3pm = float(request.form["windspeed3pm"])
            humidity9am = float(request.form["humidity9am"])
            humidity3pm = float(request.form["humidity3pm"])
            pressure9am = float(request.form["pressure9am"])
            pressure3pm = float(request.form["pressure3pm"])
            temp9am = float(request.form["temp9am"])
            temp3pm = float(request.form["temp3pm"])
            cloud9am = float(request.form["cloud9am"])
            cloud3pm = float(request.form["cloud3pm"])
            location = float(request.form["location"])
            winddDir9am = float(request.form["winddir9am"])
            winddDir3pm = float(request.form["winddir3pm"])
            windGustDir = float(request.form["windgustdir"])
            rainToday = float(request.form["raintoday"])

            # Create input list
            input_lst = [
                location, minTemp, maxTemp, rainfall, evaporation, sunshine,
                windGustDir, windGustSpeed, winddDir9am, winddDir3pm, windSpeed9am, windSpeed3pm,
                humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm,
                temp9am, temp3pm, rainToday, month, day
            ]

            # Reshape for prediction
            input_array = np.array([input_lst])
            pred = model.predict(input_array)
            output = int(pred[0])

            # Render result
            if output == 0:
                return render_template("sunny.html")
            else:
                return render_template("rainy.html")

        except Exception as e:
            return f"Error: {e}"

    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
