import streamlit as st

# Set the title of the app
st.title("User Input Form")

# Create a form to collect user inputs
with st.form(key='user_input_form'):
    # Input fields
    occupation = st.text_input("Enter your occupation:")
    age = st.number_input("Enter your age:", min_value=0)
    daily_steps = st.number_input("Enter your daily steps:", min_value=0)
    
    # User input for physical activity level (1 to 10)
    physical_activity_level = st.number_input("Enter your physical activity level (1 to 10):", 
                                               min_value=1, max_value=10)

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Display the collected inputs
        st.success("Thank you for your submission!")
        st.write(f"Occupation: {occupation}")
        st.write(f"Age: {age}")
        st.write(f"Daily Steps: {daily_steps}")
        st.write(f"Physical Activity Level: {physical_activity_level}")

