import streamlit as st
import requests

def get_text_from_sefaria(parsha):
    url = f"https://www.sefaria.org/api/texts/{parsha}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['text']
    else:
        st.error(f"Error fetching data from Sefaria: {response.status_code}")
        return None

def display_words(text):
    for chapter in text:
        for verse in chapter:
            words = verse.split()
            for word in words:
                st.write(word)

def main():
    st.title("Parshas Noach Word Display")
    
    parsha = "Genesis.6.9-11.32"  # The range of verses for Parshas Noach
    
    st.write("Fetching text from Sefaria...")
    text = get_text_from_sefaria(parsha)
    
    if text:
        st.write("Displaying words:")
        display_words(text)

if __name__ == "__main__":
    main()
