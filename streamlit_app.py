import streamlit as st
import requests
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime, timedelta
import io

def download_pdf(url):
    response = requests.get(url)
    response.raise_for_status()
    return io.BytesIO(response.content)

def combine_pdfs(pdfs):
    pdf_writer = PdfWriter()
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    combined_pdf = io.BytesIO()
    pdf_writer.write(combined_pdf)
    combined_pdf.seek(0)
    return combined_pdf

def get_pdf_urls(start_date):
    pdf_urls = []
    for i in range(2):
        pdf_number = (start_date - datetime(2024, 8, 13)).days * 2 + i + 3356
        url = f"https://daf-yomi.com/Data/UploadedFiles/DY_Page/{pdf_number}.pdf"
        pdf_urls.append(url)
    return pdf_urls

def main():
    st.title('Daily PDF Downloader and Combiner')
    
    start_date = datetime(2024, 8, 13)
    today = datetime.now().date()
    days_since_start = (today - start_date.date()).days
    date_of_interest = start_date + timedelta(days=days_since_start)
    
    st.write(f"Downloading PDFs for date: {date_of_interest.strftime('%Y-%m-%d')}")
    
    pdf_urls = get_pdf_urls(date_of_interest)
    st.write("PDF URLs:", pdf_urls)
    
    pdfs = [download_pdf(url) for url in pdf_urls]
    combined_pdf = combine_pdfs(pdfs)
    
    st.download_button(
        label="Download Combined PDF",
        data=combined_pdf,
        file_name=f"combined_{date_of_interest.strftime('%Y-%m-%d')}.pdf",
        mime="application/pdf"
    )

if __name__ == "__main__":
    main()