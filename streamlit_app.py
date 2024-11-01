import streamlit as st

# Set the title of the app
st.title("User Input Form")

# Create a form to collect user inputs
with st.form(key='user_input_form'):
    # Input fields
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)
    email = st.text_input("Enter your email:")
    favorite_color = st.selectbox("Select your favorite color:", ['Red', 'Green', 'Blue', 'Yellow', 'Purple'])

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Display the collected inputs
        st.write("Thank you for your submission!")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        st.write(f"Favorite Color: {favorite_color}")
