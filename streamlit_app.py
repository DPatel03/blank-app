import streamlit as st


st.title("User Input Form")


with st.form(key='user_input_form'):

    occupation = st.text_input("Enter your occupation:")
    age = st.number_input("Enter your age:", min_value=0)
    daily_steps = st.number_input("Enter your daily steps:", min_value=0)
    

    physical_activity_level = st.number_input("Enter your physical activity level (1 to 10):", 
                                               min_value=1, max_value=10)
    stress_level = st.number_input("Enter your stress level (1 to 10):", 
                                               min_value=1, max_value=10)


    submit_button = st.form_submit_button(label='Submit')

    if submit_button:

        st.success("Thank you for your submission!")
        st.write(f"Occupation: {occupation}")
        st.write(f"Age: {age}")
        st.write(f"Daily Steps: {daily_steps}")
        st.write(f"Physical Activity Level: {physical_activity_level}")
        st.write(f" stress_level: {stress_level}")

