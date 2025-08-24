import streamlit as st

# Set the title of the app
st.title("Love Percentage Calculator ❤️")

# Input fields
user_name = st.text_input("Enter Your Name:")
lover_name = st.text_input("Enter Your Lover's Name:")

# Button to trigger love calculation
if st.button("Calculate Love"):
    if not user_name.strip() or not lover_name.strip():
        st.error("Please enter both names!")  # Display error message
    else:
        # Convert names to lowercase for comparison
        user_lower = user_name.strip().lower()
        lover_lower = lover_name.strip().lower()

        # Base love percentage calculation
        combined = user_lower + lover_lower
        score = sum(ord(char) for char in combined)
        love_percentage = (score % 100) + 1  # Range: 1-100%

        # Special cases for Abubackar + Money
        abu_names = {"abubackar siddiq s", "abubackar siddiq", "abubackar", "abu"}

        if user_lower in abu_names and lover_lower == "money":
            love_percentage = "100 Billion"
            love_result = "This is the True Love"
        elif user_lower in abu_names:
            love_percentage = 0
            love_result = "Abubackar is already in love with Money"
        elif isinstance(love_percentage, int) and love_percentage <= 10:
            love_result = "Your Love is Low"
        elif isinstance(love_percentage, int) and 10 < love_percentage <= 40:
            love_result = "Your Love is Good"
        elif isinstance(love_percentage, int) and 40 < love_percentage <= 70:
            love_result = "Your Love is Crazy"
        else:
            love_result = "Your Love is On Peak"

        # Display the result
        st.subheader(f"{user_name.strip()} ❤ {lover_name.strip()}")
        st.write(f"Your Love: {love_percentage}%")
        st.success(f"{love_result}!")
