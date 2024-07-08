import streamlit as st
import pdfkit
import requests
import os

# Title of the app
st.title('Sefaria Psalms Link Generator and PDF Creator')

# Prompt the user to enter a number
number = st.number_input('Enter a Psalm number:', min_value=1, max_value=150, step=1)

# Generate the link
link = f'https://www.sefaria.org/Psalms.{number}?lang=he'

# Display the link
st.write('Generated Link:')
st.write(link)

# Provide a clickable link
st.markdown(f'[Click here to view Psalm {number}]({link})')

# Button to create the PDF
if st.button('Generate PDF'):
    # Fetch content from the link
    response = requests.get(link)
    html_content = response.text

    # Save the content to an HTML file
    with open('temp.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Convert HTML file to PDF
    pdf_output = f'Sefaria_Psalms_{number}.pdf'
    pdfkit.from_file('temp.html', pdf_output)

    # Provide a link to download the PDF
    with open(pdf_output, 'rb') as pdf_file:
        st.download_button('Download PDF', pdf_file, file_name=pdf_output)

    # Clean up temporary files
    os.remove('temp.html')
    os.remove(pdf_output)
