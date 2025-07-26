import random
import streamlit as st

# Set the title of the app
st.title("Love Percentage Calculator ❤️")

# Create input fields for the user's name and their lover's name
user_name = st.text_input("Enter Your Name:")
lover_name = st.text_input("Enter Your Lover's Name:")

# Button to trigger love calculation
if st.button("Calculate Love"):
    if user_name == "" or lover_name == "":
        st.error("Please enter both names!")  # Display error message
    else:
        # New deterministic love percentage calculation based on names
        combined = (user_name.strip().lower() + lover_name.strip().lower())
        score = sum(ord(char) for char in combined)
        love_percentage = (score % 100) + 1  # Ensures 1-100%
        
        # Determine the love level based on the percentage
        if user_name == "Abubackar Siddiq S" and lover_name == "Money":
            love_percentage = "100 Billion"
            love_result = "This is the True Love"
        elif user_name == "Abubackar Siddiq" and lover_name == "Money":
            love_percentage = "100 Billion"
            love_result = "This is the True Love"
        elif user_name == "Abubackar" and lover_name == "Money":
            love_percentage = "100 Billion"
            love_result = "This is the True Love"
        elif user_name == "Abu" and lover_name == "Money":
            love_percentage = "100 Billion"
            love_result = "This is the True Love"
        elif user_name == "Abubackar Siddiq S":
            love_percentage = 0
            love_result = "Abubackar is already in love with Money"
        elif user_name == "Abubackar Siddiq":
            love_percentage = 0
            love_result = "Abubackar is already in love with Money"
        elif user_name == "Abubackar":
            love_percentage = 0
            love_result = "Abubackar is already in love with Money"
        elif user_name == "Abu":
            love_percentage = 0
            love_result = "Abubackar is already in love with Money"
        elif love_percentage <= 10:
            love_result = "Your Love is Low"
        elif 10 < love_percentage <= 40:
            love_result = "Your Love is Good"
        elif 40 < love_percentage <= 70:
            love_result = "Your Love is Crazy"
        else:
            love_result = "Your Love is On Peak"
        
        # Display the result
        st.subheader(f"{user_name} ❤ {lover_name}")
        st.write(f"Your Love: {love_percentage}%")
        st.success(f"{love_result}!")
