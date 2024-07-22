import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import csv
import io

def get_hebrew_text_from_sefaria(parsha):
    url = f"https://www.sefaria.org/api/texts/{parsha}?context=0&lang=he"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['he']
    else:
        st.error(f"Error fetching data from Sefaria: {response.status_code}")
        return None

def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_trope_and_punctuation(text):
    # Trop (cantillation marks) Unicode range: U+0591 to U+05AF
    # Remove cantillation marks and colons
    return re.sub(r'[\u0591-\u05AF:]', '', text)

def export_words_to_csv(text):
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Word'])  # Write header
    for chapter in text:
        for verse in chapter:
            cleaned_verse = clean_html(verse)
            verse_without_trope = remove_trope_and_punctuation(cleaned_verse)
            words = verse_without_trope.split()  # Split the verse into words
            for word in words:
                if word:  # Check if the word is not empty
                    writer.writerow([word])
    output.seek(0)
    return output.getvalue().encode('utf-8')  # Ensure UTF-8 encoding

def main():
    st.title("Parshas Noach Word Display and Export")

    parsha = "Genesis.6.9-11.32"  # The range of verses for Parshas Noach
    
    if st.button('Fetch and Export Words'):
        st.write("Fetching text from Sefaria...")
        text = get_hebrew_text_from_sefaria(parsha)
        
        if text:
            st.write("Displaying raw Hebrew text for debugging:")
            st.write(text)  # Display raw text for debugging
            
            # Check for gibberish in the fetched text
            gibberish = any(re.search(r'[^\u0590-\u05FF\s]', verse) for chapter in text for verse in chapter)
            if gibberish:
                st.error("Gibberish detected in the fetched text!")
                return
            
            st.write("Processing and exporting words to CSV...")
            csv_data = export_words_to_csv(text)
            
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name='parshas_noach.csv',
                mime='text/csv'
            )
            st.success("Export completed.")

if __name__ == "__main__":
    main()
