import streamlit as st

# Set the title of the app
st.title("User Input Form")

# Create a form to collect user inputs
with st.form(key='user_input_form'):
    # Input fields
    name = st.text_input("Enter your name:")  # Corrected variable name
    age = st.number_input("Enter your age:", min_value=0)
    daily_steps = st.number_input("Enter your daily steps:", min_value=0)  # Changed to number_input for steps
    physical_activity_level = st.input("Select your physical activity level:" )  # Provided options for selectbox

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Display the collected inputs
        st.success("Thank you for your submission!")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Daily Steps: {daily_steps}")  # Corrected output label
        st.write(f"Physical Activity Level: {physical_activity_level}")  # Corrected output label
