# ML-Based Rainfall Prediction Web Application

A web application that uses machine learning to predict whether it will rain tomorrow based on current weather conditions. The system utilizes an XGBoost model trained on Australian weather data.

![Rainfall Prediction App](https://api/placeholder/800/400)

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
   cd rainfall-prediction
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

5. Open your web browser and visit `http://localhost:5000`

## Project Structure

```
rainfall-prediction/
├── app.py                  # Flask application file
├── template/               # HTML templates
│   ├── home.html           # Main form page
│   ├── sunny.html          # Result page for sunny prediction
│   ├── rainy.html          # Result page for rainy prediction
├── static/                 # Static assets
│   ├── predictor.css       # Main CSS for form
│   ├── result.css          # CSS for result pages
│   ├── sunny.svg           # Sunny day illustration
│   ├── rainy.svg           # Rainy day illustration
├── xgboostmodel.pkl        # Trained XGBoost model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Australian Bureau of Meteorology for the weather dataset
- XGBoost team for the excellent machine learning library
- Flask team for the web framework
