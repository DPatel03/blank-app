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
st.set_page_config(
    page_title="Sleep Quality Predictor",
    page_icon="🛌",
    layout="wide",
)

# Function to load Lottie animation



# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #e8f5e9;
            font-family: 'Arial', sans-serif;
        }
        .main {
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2e7d32;
        }
        .stButton button {
            background-color: #66bb6a !important;
            color: white !important;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #43a047 !important;
        }
        .block-container {
            padding: 2rem 3rem;
        }
        .separator {
            border: none;
            height: 2px;
            background: linear-gradient(to right, #43a047, #2e7d32);
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Header with Animation
col1, col2 = st.columns([2, 1])
with col1:
    st.title("🌟 Sleep Quality Predictor")
    st.write("#### Your personalized tool to understand your sleep habits.")
    st.markdown("<hr class='separator'>", unsafe_allow_html=True)
with col2:
    st_lottie(lottie_sleep, height=150, key="sleep_animation")

# Progress Tracker
st.subheader("Step 1: Enter Your Information")

# Basic Information Section
with st.form(key='user_input_form'):
    col1, col2 = st.columns(2)
    with col1:
        occupation = st.text_input("Occupation", placeholder="Enter your occupation")
    with col2:
        age = st.number_input("Age", min_value=0, max_value=120, step=1, help="Enter your age (0-120)")
    
    col3, col4 = st.columns(2)
    with col3:
        daily_steps = st.number_input("Daily Steps", min_value=0, step=100, help="Enter your average daily step count")
    with col4:
        heart_rate = st.number_input("Heart Rate", min_value=0, step=1, help="Enter your resting heart rate")

    st.markdown("<hr class='separator'>", unsafe_allow_html=True)

    # Lifestyle Factors Section
    st.subheader("Step 2: Rate Your Lifestyle")
    col5, col6 = st.columns(2)
    with col5:
        physical_activity_level = st.slider(
            "Physical Activity Level", 
            min_value=1, 
            max_value=10, 
            value=5, 
            help="1 = Very low activity, 10 = Very high activity"
        )
    with col6:
        stress_level = st.slider(
            "Stress Level", 
            min_value=1, 
            max_value=10, 
            value=5, 
            help="1 = Very low stress, 10 = Very high stress"
        )

    sleep_duration = st.number_input(
        "Sleep Duration (in hours)", 
        min_value=0.0, 
        max_value=24.0, 
        value=5.0, 
        step=0.5, 
        help="Enter the number of hours you sleep per day (e.g., 7.5)"
    )
    
    st.markdown("<hr class='separator'>", unsafe_allow_html=True)

    submit_button = st.form_submit_button(label="📤 Submit")

if submit_button:
    if not occupation:
        st.error("🚨 Please enter your occupation.")
    elif age == 0:
        st.error("🚨 Please enter a valid age.")
    elif daily_steps == 0:
        st.error("🚨 Please enter your daily steps.")
    else:
        st.success("✅ Thank you for your submission!")
        
        st.markdown("<hr class='separator'>", unsafe_allow_html=True)
        st.subheader("Your Submission:")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Occupation:** {occupation}")
            st.write(f"**Age:** {age}")
            st.write(f"**Daily Steps:** {daily_steps}")
        with col2:
            st.write(f"**Heart Rate:** {heart_rate}")  
            st.write(f"**Sleep Duration:** {sleep_duration}")         
            st.write(f"**Physical Activity Level:** {physical_activity_level}")
            st.write(f"**Stress Level:** {stress_level}")
        
        st.markdown("<hr class='separator'>", unsafe_allow_html=True)
        # sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate)
        # st.subheader(f"🌙 Predicted Sleep Quality: {sleep_quality}")


            # sleep quality determiner
            # sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate)
            # st.write(f"**Sleep Quality:** {sleep_quality}")
