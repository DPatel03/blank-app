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

import streamlit as st
import pandas as pd

# ---------------------------- STYLING ----------------------------
st.set_page_config(page_title="Sleep Quality Predictor", page_icon="💤", layout="wide")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom right, #4facfe, #00f2fe);
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: bold;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        color: white;
        font-size: 1.5rem;
        margin-bottom: 40px;
    }
    .card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        margin: auto;
        max-width: 700px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
    }
    .btn-submit {
        background-color: #0078d7;
        color: white;
        font-size: 1.2rem;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        border: none;
    }
    .btn-submit:hover {
        background-color: #005bb5;
    }
    .result-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 20px auto;
        max-width: 700px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
    }
    .result-text {
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
        color: #0078d7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------- HEADER ----------------------------
st.markdown('<div class="title">Sleep Quality Predictor</div>', unsafe_allow_html=True)

# ---------------------------- FORM ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("User Input Form")
with st.form(key="user_input_form"):
    # Occupation and Age Fields
    col1, col2 = st.columns(2)
    with col1:
        occupation = st.text_input("Occupation", placeholder="Enter your occupation")
    with col2:
        age = st.number_input("Age", min_value=0, max_value=120, help="Enter your age (0-120)")

    # Daily Steps and Heart Rate
    col3, col4 = st.columns(2)
    with col3:
        daily_steps = st.number_input("Daily Steps", min_value=0, step=100, help="Enter your average daily step count")
    with col4:
        heart_rate = st.number_input("Heart Rate", min_value=0, step=1, help="Enter your heart rate")

    # Lifestyle Factors Section
    st.subheader("Lifestyle Factors")
    col5, col6, col7 = st.columns(3)
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
    with col7:
        sleep_duration = st.number_input("Sleep Duration (hours)", min_value=1, max_value=15, step=1, help="Enter sleep duration in hours")
    
    # Submit Button
    submit_button = st.form_submit_button(label="Predict Sleep Quality", type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------- PREDICTION ----------------------------
if submit_button:
    if not occupation:
        st.error("Please enter your occupation.")
    elif age == 0:
        st.error("Please enter a valid age.")
    elif daily_steps == 0:
        st.error("Please enter your daily steps.")
    else:
       

        # # Display Result
        # st.markdown('<div class="result-card">', unsafe_allow_html=True)
        # st.markdown(
        #     f"""
        #     <div class="result-text">
        #         Based on your inputs, your predicted sleep quality is: <strong>{predicted_quality}</strong>.
        #     </div>
        #     """,
        #     unsafe_allow_html=True,
        # )
        # st.markdown('</div>', unsafe_allow_html=True)



            # sleep quality determiner
            # sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate)
            # st.write(f"**Sleep Quality:** {sleep_quality}")
