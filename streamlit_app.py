import streamlit as st

# Predefined dictionary simulating sources
sources = {
    'Shabbat': 'Shulchan Aruch, Orach Chayim 242:1',
    'Kashrut': 'Yoreh De\'ah 87:1',
    'Tefillin': 'Shulchan Aruch, Orach Chayim 25:1',
    'Lashon Hara': 'Chofetz Chaim, Introduction:1',
    'Bracha Rishona': 'Shulchan Aruch, Orach Chayim 206:1',
    'Bracha Acharona': 'Shulchan Aruch, Orach Chayim 208:1'
}

def main():
    st.title("Torah Sources Finder")
    st.write("Enter any topic, subject, halacha, or posek to find its source.")

    query = st.text_input("Enter your query:")
    if st.button("Find Source"):
        source = sources.get(query)
        if source:
            st.success(f"Source: {source}")
        else:
            st.error("Source not found. Please try another query.")

if __name__ == "__main__":
    main()
