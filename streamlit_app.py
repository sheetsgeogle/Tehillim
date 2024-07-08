import streamlit as st

# Title of the app
st.title('Sefaria Psalms Link Generator')

# Prompt the user to enter a number
number = st.number_input('Enter a Psalm number:', min_value=1, max_value=150, step=1)

# Generate the link
link = f'https://www.sefaria.org/Psalms.{number}?lang=he'

# Display the link
st.write('Generated Link:')
st.write(link)

# Provide a clickable link
st.markdown(f'[Click here to view Psalm {number}]({link})')
