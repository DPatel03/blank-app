import streamlit as st

# Title
st.title("User Input Form")

# Basic Information Section
st.header("Basic Information")
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

    # Lifestyle Factors Section
    st.header("Lifestyle Factors")
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
    
    # Submit Button
    submit_button = st.form_submit_button(label="Submit")

    # Check if any fields are missing
    if submit_button:
        if not occupation:
            st.error("Please enter your occupation.")
        elif age == 0:
            st.error("Please enter a valid age.")
        elif daily_steps == 0:
            st.error("Please enter your daily steps.")
        elif physical_activity_level < 1 or physical_activity_level > 10:
            st.error("Please enter a physical activity level between 1 and 10.")
        elif stress_level < 1 or stress_level > 10:
            st.error("Please enter a stress level between 1 and 10.")
        else:
            # All fields are filled, show success message
            st.success("Thank you for your submission!")
            
            # Display User's Input
            st.write("### Submitted Information")
            st.write(f"**Occupation:** {occupation}")
            st.write(f"**Age:** {age}")
            st.write(f"**Daily Steps:** {daily_steps}")
            st.write(f"**Physical Activity Level:** {physical_activity_level}")
            st.write(f"**Stress Level:** {stress_level}")
