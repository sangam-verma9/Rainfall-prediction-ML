# ML-Based Rainfall Prediction Web Application

A web application that uses machine learning to predict whether it will rain tomorrow based on current weather conditions. The system utilizes an XGBoost model trained on Australian weather data.

## 🌐 Live Demo

[![View Demo](https://img.shields.io/badge/View-Demo-blue)](https://rainfallpredictor.onrender.com)

<a href="https://rainfallpredictor.onrender.com" target="_blank">
  <img src="https://api.microlink.io/?url=https://rainfallpredictor.onrender.com&screenshot=true&meta=false&embed=screenshot.url" alt="Rainfall Prediction App Screenshot" />
</a>

## Features

- Predict tomorrow's rainfall using machine learning
- User-friendly form interface to input weather data
- Interactive result pages for sunny and rainy predictions
- Responsive design that works on desktop and mobile devices

## Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: XGBoost
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Font Awesome icons
- **Data Processing**: Pandas, NumPy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/sangam-verma9/Rainfall-prediction-ML.git
   cd Rainfall-prediction-ML
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and visit `http://127.0.0.1:5000/`

## Project Structure

```
RAINFALL-PREDICTION-ML/
├── static/                  # Static assets
│   ├── predictor.css        # Main CSS for form
│   ├── result.css           # CSS for result pages
│   ├── sunny.svg            # Sunny day illustration
│   ├── rainy.svg            # Rainy day illustration
├── template/                # HTML templates
│   ├── home.html            # Main form page
│   ├── sunny.html           # Result page for sunny prediction
│   ├── rainy.html           # Result page for rainy prediction
├── app.py                   # Flask application file
├── xgboostmodel.pkl         # Trained XGBoost model
├── catboost_model.ipynb     # Notebook for CatBoost model
├── catboost_model.pkl       # Trained CatBoost model
├── Data Preprocessing.ipynb # Data preprocessing notebook
├── Decision Tree model.ipynb # Decision Tree model notebook
├── decision_tree_model.pkl  # Trained Decision Tree model
├── Feature selection.ipynb  # Feature selection analysis notebook
├── KNeighbors Classifier model.ipynb # KNN model notebook
├── kneighbors_model.pkl     # Trained KNN model
├── Logistic Regression model.ipynb # Logistic Regression notebook
├── LogisticRegression_model.pkl # Trained Logistic Regression model
├── Random Forest model.ipynb # Random Forest model notebook
├── requirements.txt         # Python dependencies
├── weather_preprocessed.csv # Preprocessed weather data
├── weatherAUS.csv           # Original Australian weather dataset
├── Xgboost model.ipynb      # XGBoost model notebook
└── README.md                # Project documentation

```

## Input Features

The model requires the following weather parameters:

- **Date Information**: Day and month
- **Temperature Data**: Minimum, maximum, 9am, and 3pm temperatures
- **Weather Conditions**: Rainfall, evaporation, sunshine, and rain today status
- **Wind Information**: Wind direction and speed at different times of day
- **Humidity and Pressure**: Measurements at 9am and 3pm
- **Cloud Cover**: Measurements at 9am and 3pm
- **Location**: Selected from a list of Australian weather stations

## Model Information

The prediction is powered by an XGBoost classifier trained on historical Australian weather data. The model takes current weather conditions as input and predicts a binary outcome:
- 0: No rain tomorrow (sunny)
- 1: Rain tomorrow (rainy)

## Future Improvements

- Add data visualization for weather trends
- Implement geolocation to automatically detect user location
- Add multi-day forecasting capabilities
- Create a mobile app version
- Add user accounts to save previous predictions

## Acknowledgments

- Australian Bureau of Meteorology for the weather dataset
- XGBoost team for the excellent machine learning library
- Flask team for the web framework
