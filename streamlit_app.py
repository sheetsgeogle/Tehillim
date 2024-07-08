import streamlit as st
from fpdf import FPDF

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

# Button to create the PDF
if st.button('Generate PDF'):
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt=f'Sefaria Psalms Link for Psalm {number}', ln=True, align='C')
    pdf.cell(200, 10, txt=link, ln=True, align='C')

    # Save PDF to a file
    pdf_output = f'Sefaria_Psalms_{number}.pdf'
    pdf.output(pdf_output)

    # Provide a link to download the PDF
    with open(pdf_output, 'rb') as pdf_file:
        st.download_button('Download PDF', pdf_file, file_name=pdf_output)
