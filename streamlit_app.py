import streamlit as st

# Set the title of the app
st.title("User Input Form")

# Create a form to collect user inputs
with st.form(key='user_input_form'):
    # Input fields
    occupation = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)
    daily_steps = st.text_input("Enter your daily steps:")
    physical_activity_level = st.selectbox("Enter your pyhsical activity level")

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Display the collected inputs
        st.write("Thank you for your submission!")
        st.write(f"Name: {occupation}")
        st.write(f"Age: {age}")
        st.write(f"Email: {daily_steps}")
        st.write(f"Favorite Color: {physical_activity_level}")
