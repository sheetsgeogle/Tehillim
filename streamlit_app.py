import streamlit as st
import time
from datetime import datetime

# Function to display the current time in 12-hour format
def display_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    return current_time

# Main function to run the Streamlit app
def main():
    st.title("Alarm Clock")
    
    # User inputs for font size and color
    font_size = st.sidebar.slider("Font Size", 10, 100, 50)
    font_color = st.sidebar.color_picker("Font Color", "#FFFFFF")
    
    # User input for setting an alarm
    alarm_time = st.sidebar.text_input("Set Alarm (HH:MM:SS AM/PM)", "12:00:00 AM")
    
    # Create a placeholder for the time display
    time_display = st.empty()
    
    while True:
        # Display the current time with custom font size and color
        current_time = display_time()
        time_display.markdown(
            f"<h1 style='text-align: center; color: {font_color}; font-size: {font_size}px;'>{current_time}</h1>",
            unsafe_allow_html=True
        )
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            st.warning("⏰ It's time!")
        
        # Pause for a second before updating the time display
        time.sleep(1)

if __name__ == "__main__":
    main()
