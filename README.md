# 💤 ZzzPredict 💤

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### About the Project

Our project is called ZzzPredict. It aims to predict sleep quality given information such as age, daily step count, sleep duration, etc.

Many people often do not realize the impact of their daily habits on their sleep quality. With this predictor they will be able to see what factors affect their sleep quality, as well as learn what they need to change in order to improve their quality of sleep.

It is beneficial for people to understand and be aware of their sleep quality, as getting enough sleep is a major factor of staying healthy.

### Set Up

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
### Using the App

1. Input requested information.
2. Submit information.
3. Recieve sleep quality score and rating as output.

### Process

1. Determining most relevant features using correlation matrix and feature importance function.
2. Building relevant model: Random Forest Regressor.
3. Training the model with Sleep Data dataset.
4. Developing interactive Streamlit app to display model predictions.
