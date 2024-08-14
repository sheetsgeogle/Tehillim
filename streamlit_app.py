import streamlit as st
import requests
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime, timedelta
import io
import streamlit_toggle as stt

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
    st.title('Gemara Library')

    # Dropdown for Gemara Type and Mesechta
    option = st.selectbox(
        "Select Gemara Type:",
        ["Standard", "Artscroll", "Mesivta", "Koren"]
    )

    mesechta = st.selectbox(
        "Select Mesechta:",
        [
            "ברכות", "כריתות", "הוריות", "מגילה", "סנהדרין", "תענית", "מועד קטן",
            "סוטה", "ערכין", "מכות", "שבת", "קידושין", "חגיגה", "בבא מציעא",
            "בבא קמא", "עבודה זרה", "תמורה", "נידה", "יבמות", "ראש השנה",
            "פסחים", "גיטין", "בכורות", "שבועות", "מנחות", "כתובות", "יומא",
            "עירובין", "ביצה", "חולין", "סוכה", "זבחים", "תמיד", "בבא בתרא",
            "נזיר", "מעילה", "נדרים"
        ]
    )

    # Daf Yomi toggle
    daf_yomi_toggle = stt.st_toggle_switch(
        label='Daf Yomi (Off/On)',
        default_value=False,  # Default to Off
        label_after=True,
        inactive_color='#780c21',  # Red when Off
        active_color='#0c7822',  # Green when On
        track_color='#0c4c78'  # Blue track color
    )

    if daf_yomi_toggle:
        # Calculate the current day's Daf Yomi page numbers
        start_date = datetime(2024, 8, 13)
        today = datetime.now().date()
        days_since_start = (today - start_date.date()).days
        date_of_interest = start_date + timedelta(days=days_since_start)
        
        pdf_urls = get_pdf_urls(date_of_interest)
        pdfs = [download_pdf(url) for url in pdf_urls]
        combined_pdf = combine_pdfs(pdfs)

        st.download_button(
            label="Download today's Daf Yomi PDF",
            data=combined_pdf,
            file_name=f"combined_{date_of_interest.strftime('%Y-%m-%d')}.pdf",
            mime="application/pdf"
        )
    else:
        # URL patterns for different Gemara types and Mesechtot
        url_patterns = {
            "Standard": {
                "ברכות": "https://example.com/standard/berachot.pdf",
                "כריתות": "https://example.com/standard/keritot.pdf",
                "הוריות": "https://example.com/standard/horayot.pdf",
                "מגילה": "https://example.com/standard/megillah.pdf",
                "סנהדרין": "https://example.com/standard/sanhedrin.pdf",
                "תענית": "https://example.com/standard/taanit.pdf",
                "מועד קטן": "https://example.com/standard/moed_katan.pdf",
                "סוטה": "https://example.com/standard/sotah.pdf",
                "ערכין": "https://example.com/standard/erukhin.pdf",
                "מכות": "https://example.com/standard/makkot.pdf",
                "שבת": "https://example.com/standard/shabbat.pdf",
                "קידושין": "https://example.com/standard/kiddushin.pdf",
                "חגיגה": "https://example.com/standard/chagigah.pdf",
                "בבא מציעא": "https://example.com/standard/baba_metzia.pdf",
                "בבא קמא": "https://example.com/standard/baba_kamma.pdf",
                "עבודה זרה": "https://example.com/standard/avodah_zarah.pdf",
                "תמורה": "https://example.com/standard/temurah.pdf",
                "נידה": "https://example.com/standard/niddah.pdf",
                "יבמות": "https://example.com/standard/yevamot.pdf",
                "ראש השנה": "https://example.com/standard/rosh_hashanah.pdf",
                "פסחים": "https://example.com/standard/psachim.pdf",
                "גיטין": "https://example.com/standard/gittin.pdf",
                "בכורות": "https://example.com/standard/bechorot.pdf",
                "שבועות": "https://example.com/standard/shevuot.pdf",
                "מנחות": "https://example.com/standard/menachot.pdf",
                "כתובות": "https://example.com/standard/ketubot.pdf",
                "יומא": "https://example.com/standard/yoma.pdf",
                "עירובין": "https://example.com/standard/eruvin.pdf",
                "ביצה": "https://example.com/standard/beitzah.pdf",
                "חולין": "https://example.com/standard/chullin.pdf",
                "סוכה": "https://example.com/standard/sukkah.pdf",
                "זבחים": "https://example.com/standard/zevachim.pdf",
                "תמיד": "https://example.com/standard/tamid.pdf",
                "בבא בתרא": "https://example.com/standard/baba_batra.pdf",
                "נזיר": "https://example.com/standard/nazir.pdf",
                "מעילה": "https://example.com/standard/meilah.pdf",
                "נדרים": "https://example.com/standard/nedarim.pdf"
            },
            "Artscroll": {
                "ברכות": "https://example.com/artscroll/berachot.pdf",
                "כריתות": "https://example.com/artscroll/keritot.pdf",
                "הוריות": "https://example.com/artscroll/horayot.pdf",
                "מגילה": "https://example.com/artscroll/megillah.pdf",
                "סנהדרין": "https://example.com/artscroll/sanhedrin.pdf",
                "תענית": "https://example.com/artscroll/taanit.pdf",
                "מועד קטן": "https://example.com/artscroll/moed_katan.pdf",
                "סוטה": "https://example.com/artscroll/sotah.pdf",
                "ערכין": "https://example.com/artscroll/erukhin.pdf",
                "מכות": "https://example.com/artscroll/makkot.pdf",
                "שבת": "https://example.com/artscroll/shabbat.pdf",
                "קידושין": "https://example.com/artscroll/kiddushin.pdf",
                "חגיגה": "https://example.com/artscroll/chagigah.pdf",
                "בבא מציעא": "https://example.com/artscroll/baba_metzia.pdf",
                "בבא קמא": "https://example.com/artscroll/baba_kamma.pdf",
                "עבודה זרה": "https://example.com/artscroll/avodah_zarah.pdf",
                "תמורה": "https://example.com/artscroll/temurah.pdf",
                "נידה": "https://example.com/artscroll/niddah.pdf",
                "יבמות": "https://example.com/artscroll/yevamot.pdf",
                "ראש השנה": "https://example.com/artscroll/rosh_hashanah.pdf",
                "פסחים": "https://example.com/artscroll/psachim.pdf",
                "גיטין": "https://example.com/artscroll/gittin.pdf",
                "בכורות": "https://example.com/artscroll/bechorot.pdf",
                "שבועות": "https://example.com/artscroll/shevuot.pdf",
                "מנחות": "https://example.com/artscroll/menachot.pdf",
                "כתובות": "https://example.com/artscroll/ketubot.pdf",
                "יומא": "https://example.com/artscroll/yoma.pdf",
                "עירובין": "https://example.com/artscroll/eruvin.pdf",
                "ביצה": "https://example.com/artscroll/beitzah.pdf",
                "חולין": "https://example.com/artscroll/chullin.pdf",
                "סוכה": "https://example.com/artscroll/sukkah.pdf",
                "זבחים": "https://example.com/artscroll/zevachim.pdf",
                "תמיד": "https://example.com/artscroll/tamid.pdf",
                "בבא בתרא": "https://example.com/artscroll/baba_batra.pdf",
                "נזיר": "https://example.com/artscroll/nazir.pdf",
                "מעילה": "https://example.com/artscroll/meilah.pdf",
                "נדרים": "https://example.com/artscroll/nedarim.pdf"
            },
            "Mesivta": {
                # Add Mesivta URLs here
            },
            "Koren": {
                # Add Koren URLs here
            }
        }

        selected_url = url_patterns[option].get(mesechta, None)

        if selected_url:
            pdf = download_pdf(selected_url)
            st.download_button(
                label=f"Download {mesechta} ({option}) PDF",
                data=pdf,
                file_name=f"{mesechta}_{option}.pdf",
                mime="application/pdf"
            )
        else:
            st.write("PDF not available for the selected options.")

if __name__ == "__main__":
    main()
