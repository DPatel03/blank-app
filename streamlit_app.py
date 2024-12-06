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
# def produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate, occupation):
#     # Hold user input
#     user_input = {
#         'Age': age,
#         'Daily Steps': daily_steps,
#         'Physical Activity Level': physical_activity_level,
#         'Stress Level': stress_level,
#         'Sleep Duration': sleep_duration,
#         'Heart Rate': heart_rate,
#         'Occupation': occupation  # Directly add the occupation integer
#     }

#     # Create DataFrame from user input
#     user_input_df = pd.DataFrame([user_input])

#     # Align DataFrame columns to match model's expected input
#     expected_columns = list(rf.feature_names_in_)
#     user_input_df = user_input_df.reindex(columns=expected_columns, fill_value=0)

#     # Predict using model
#     pred_rf = rf.predict(user_input_df)
#     print(pred_rf)
#     return pred_rf[0]

# fixed version
def produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate, occupation):
    # Map occupation to integer
    occupation_mapping = {
        "Nurse": 1,
        "Teacher": 2,
        "Salesperson": 3,
        "Doctor": 4,
        "Engineer": 5,
        "Lawyer": 6,
        "Accountant": 7,
        "Scientist": 8,
        "Software Engineer": 9,
        "Sales Representative": 10,
        "Manager": 11,
    }
    occupation_encoded = occupation_mapping.get(occupation, 0)

    # Prepare input data
    user_input = {
        'Age': age,
        'Daily Steps': daily_steps,
        'Physical Activity Level': physical_activity_level,
        'Stress Level': stress_level,
        'Sleep Duration': sleep_duration,
        'Heart Rate': heart_rate,
        'Occupation': occupation_encoded,
    }

    # Create DataFrame
    user_input_df = pd.DataFrame([user_input])

    # Align columns with model's expected input
    expected_columns = list(rf.feature_names_in_)
    user_input_df = user_input_df.reindex(columns=expected_columns, fill_value=0)

    # Predict using model
    pred_rf = rf.predict(user_input_df)
    return pred_rf[0]



# ---------------------------- STYLING ----------------------------


st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: #050b2b;
        font-family: 'Arial', sans-serif;
        padding-top: 0;
    }
    .title {
        text-align: center;
        color: white;
        font-size: 4rem;
        font-weight: bold;
        margin-top: 0;
    }
    .subtitle {
        text-align: center;
        color: white;
        font-size: 1.2rem;
        margin-bottom: 35px;
    }
    .card {
        background: transparent;
        padding: 0px;
        margin: auto;
        max-width: 700px;
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
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #0078d7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------- HEADER ----------------------------

st.markdown('<div class="title">💤 ZzzPredict 💤</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A Sleep Quality Prediction Model</div>', unsafe_allow_html=True)

# ---------------------------- FORM ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

# st.header("User Input Form")
with st.form(key="user-input-form"):
    # Occupation and Age Fields
    col1, col2 = st.columns(2)
    with col1:
    # Select occupation from predefined list
        occupation = st.selectbox(
            "Select Occupation",
            [""] + [
                "Nurse",
                "Teacher",
                "Salesperson",
                "Doctor",
                "Engineer",
                "Lawyer",
                "Accountant",
                "Scientist",
                "Software Engineer",
                "Sales Representative",
                "Manager",
            ],
            index=0,
            help="Choose your occupation from the list",
        )
    with col2:
        age = st.number_input(
            "Age",
            min_value=0,
            max_value=90,
            value=0,  
            help="Enter your age (5-90)",
        )

     # Daily Steps and Heart Rate
    col3, col4 = st.columns(2)
    with col3:
        daily_steps = st.number_input(
            "Daily Steps",
            min_value=0,
            max_value=75000,
            step=100,
            value=0,  # Default to 0
            help="Enter your average daily step count",
        )
    with col4:
        heart_rate = st.number_input(
            "Heart Rate",
            min_value=0,
            max_value=170,
            step=1,
            value=0,  # Default to 0
            help="Enter your heart rate (40-170 bpm)",
        )

    # Lifestyle Factors Section
    st.subheader("Lifestyle Factors")
    col5, col6, col7 = st.columns(3)
    with col5:
        physical_activity_level = st.slider(
            "Physical Activity Level",
            min_value=0,
            max_value=10,
            value=0,  # Default to 0
            help="1 = Very low activity, 10 = Very high activity",
        )
    with col6:
        stress_level = st.slider(
            "Stress Level",
            min_value=0,
            max_value=10,
            value=0,  # Default to 0
            help="1 = Very low stress, 10 = Very high stress",
        )
    with col7:
        sleep_duration = st.number_input(
            "Sleep Duration (hours)",
            min_value=0,
            max_value=10,
            step=1,
            value=0,  # Default to 0
            help="Enter sleep duration in hours",
        )

    
    # Submit Button
    submit_button = st.form_submit_button(label="Predict Sleep Quality", type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------- PREDICTION ----------------------------
# Submit Button
if submit_button:
    # Display the user inputs after submission
    # st.write(f"**Occupation:** {occupation}")
    # st.write(f"**Age:** {age}")
    # st.write(f"**Daily Steps:** {daily_steps}")
    # st.write(f"**Heart Rate:** {heart_rate}")  
    # st.write(f"**Sleep Duration:** {sleep_duration}")         
    # st.write(f"**Physical Activity Level:** {physical_activity_level}")
    # st.write(f"**Stress Level:** {stress_level}")
    # Call the prediction function
    sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate, occupation)
    
    # Display the prediction result
    if sleep_quality > sleep_duration:
        sleep_quality = sleep_duration
    st.markdown(f'<div class="result-text">Sleep Quality Score: {sleep_quality}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    # Display Sleep Quality Rating with Color Coding
    prediction = sleep_quality
    if prediction >= 8:
        quality = "Excellent"
        color = "darkgreen"
    elif prediction >= 6:
        quality = "Good"
        color = "green"
    elif prediction >= 4:
        quality = "Fair"
        color = "orange"
    else:
        quality = "Poor"
        color = "red"

    # Render the rating with color
    st.markdown(f'<h3 style="color: {color}; text-align: center;">Sleep Quality Rating: {quality}</h3>', unsafe_allow_html=True)


    
# sleep quality determiner
# sleep_quality = produce_output(age, daily_steps, physical_activity_level, stress_level, sleep_duration, heart_rate, occupation)
# st.write(f"**Sleep Quality:** {sleep_quality}")


