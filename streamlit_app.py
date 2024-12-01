import joblib
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import requests


# load trained model
# rf_model = joblib.load("sleep-quality-regressor.joblib")

# # define function that produces output
# def produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate):
    
#     # hold user input
#     user_input = {
#     'Sleep Duration': sleep_duration,
#     'Stress Level': stress_level,
#     'Age': age,
#     'Heart Rate': heart_rate,
#     'Physical Activity Level': physical_activity_level,
#     'Daily Steps': daily_steps
#     }

#     # dataframe to hold input
#     user_input_df = pd.DataFrame([user_input])
#     # print(user_input_df)

#     # predict using model
#     pred_rf = rf_model.predict(user_input_df)

#     return pred_rf[0]

# -------------------------------------- APP --------------------------------------------

# Title
st.title("User Input Form")

# Page Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .main-content {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    .form-header {
        color: #0073e6;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Basic Information Section
st.markdown('<h2 class="form-header">Basic Information</h2>', unsafe_allow_html=True)
with st.form(key='user_input_form'):
    st.write("Please provide some basic information about yourself.")
    
    # Occupation and Age Fields
    col1, col2 = st.columns(2)
    with col1:
        occupation = st.text_input("Occupation", placeholder="Enter your occupation")
    with col2:
        age = st.number_input("Age", min_value=0, max_value=120, help="Enter your age (0-120)")
    
    # Daily Steps
    daily_steps = st.number_input("Daily Steps", min_value=0, step=100, help="Enter your average daily step count")
    
    # Heart Rate
    heart_rate = st.number_input("Heart Rate", min_value=0, step=1, help="Enter your heart rate")

    # Lifestyle Factors Section
    st.markdown('<h2 class="form-header">Lifestyle Factors</h2>', unsafe_allow_html=True)
    st.write("Rate the following factors on a scale from 1 to 10.")
    
    # Physical Activity Level
    physical_activity_level = st.slider(
        "Physical Activity Level", 
        min_value=1, 
        max_value=10, 
        value=5, 
        help="1 = Very low activity, 10 = Very high activity"
    )
    
    # Stress Level
    stress_level = st.slider(
        "Stress Level", 
        min_value=1, 
        max_value=10, 
        value=5, 
        help="1 = Very low stress, 10 = Very high stress"
    )

    # Sleep Duration
    sleep_duration = st.number_input("Sleep Duration (hours)", min_value=1, max_value=15, step=1, help="Enter sleep duration in hours")
    
    # Submit Button
    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if not occupation:
            st.error("Please enter your occupation.")
        elif age == 0:
            st.error("Please enter a valid age.")
        elif daily_steps == 0:
            st.error("Please enter your daily steps.")
        else:
            # Display User's Input
            st.success("Thank you for your submission!")
            st.write("### Submitted Information")
            st.write(f"**Occupation:** {occupation}")
            st.write(f"**Age:** {age}")
            st.write(f"**Daily Steps:** {daily_steps}")
            st.write(f"**Heart Rate:** {heart_rate}")
            st.write(f"**Sleep Duration:** {sleep_duration}")         
            st.write(f"**Physical Activity Level:** {physical_activity_level}")
            st.write(f"**Stress Level:** {stress_level}")

st.markdown('</div>', unsafe_allow_html=True)


            # sleep quality determiner
            # sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate)
            # st.write(f"**Sleep Quality:** {sleep_quality}")
