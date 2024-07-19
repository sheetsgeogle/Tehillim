import streamlit as st
import requests
from bs4 import BeautifulSoup

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

def display_words(text):
    for chapter in text:
        for verse in chapter:
            words = verse.split()
            for word in words:
                st.write(word)

def main():
    st.title("Parshas Noach Word Display (Hebrew)")
    
    parsha = "Genesis.6.9-11.32"  # The range of verses for Parshas Noach
    
    st.write("Fetching text from Sefaria...")
    text = get_hebrew_text_from_sefaria(parsha)
    
    if text:
        st.write("Displaying words:")
        clean_text = [clean_html(verse) for chapter in text for verse in chapter]
        display_words(clean_text)

if __name__ == "__main__":
    main()
