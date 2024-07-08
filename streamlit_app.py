import streamlit as st
import requests
from pyppeteer import launch
import asyncio
import nest_asyncio

# Apply the nest_asyncio patch
nest_asyncio.apply()

# Function to generate PDF using pyppeteer
async def generate_pdf(url, output_path):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url, {'waitUntil': 'networkidle0'})
    await page.pdf({'path': output_path, 'format': 'A4'})
    await browser.close()

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
    pdf_output = f'Sefaria_Psalms_{number}.pdf'
    
    # Run the async function to generate PDF
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_pdf(link, pdf_output))

    # Provide a link to download the PDF
    with open(pdf_output, 'rb') as pdf_file:
        st.download_button('Download PDF', pdf_file, file_name=pdf_output)
