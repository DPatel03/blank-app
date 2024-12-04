import pickle
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Sleep Quality Predictor", page_icon="💤", layout="wide")
# with open('rf.sav', 'rb') as f:
#     rf = pickle.load(f)

# load trained model
@st.cache_resource
def load_rf():
    with open('rf.sav', 'rb') as f:
        rf = pickle.load(f)
    return rf
rf = load_rf()

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
#     pred_rf = rf.predict(user_input_df)
#     print(pred_rf)
#     return pred_rf[0]

# Ensure features match those used during training
def produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate, occupation):
    # Hold user input
    user_input = {
        'Age': age,
        'Daily Steps': daily_steps,
        'Physical Activity Level': physical_activity_level,
        'Stress Level': stress_level,
        'Sleep Duration': sleep_duration,
        'Heart Rate': heart_rate,
        'Occupation': occupation  # Directly add the occupation integer
    }

    # Create DataFrame from user input
    user_input_df = pd.DataFrame([user_input])

    # Align DataFrame columns to match model's expected input
    expected_columns = list(rf.feature_names_in_)
    user_input_df = user_input_df.reindex(columns=expected_columns, fill_value=0)

    # Predict using model
    pred_rf = rf.predict(user_input_df)
    print(pred_rf)
    return pred_rf[0]





# ---------------------------- STYLING ----------------------------


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
        age = st.number_input("Age", min_value=0, max_value=100, help="Enter your age (0-100)")

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
# Submit Button
# if submit_button:
#     # Display the user inputs after submission
#     st.write(f"**Occupation:** {occupation}")
#     st.write(f"**Age:** {age}")
#     st.write(f"**Daily Steps:** {daily_steps}")
#     st.write(f"**Heart Rate:** {heart_rate}")  
#     st.write(f"**Sleep Duration:** {sleep_duration}")         
#     st.write(f"**Physical Activity Level:** {physical_activity_level}")
#     st.write(f"**Stress Level:** {stress_level}")
    


# sleep quality determiner
sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate, occupation)
st.write(f"**Sleep Quality:** {sleep_quality}")
