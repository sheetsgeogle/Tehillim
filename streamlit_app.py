import streamlit as st
from transformers import pipeline

# Load a pre-trained question-answering model
nlp = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Sample context to provide to the model
context = """
The primary source for observing Shabbat is found in the Torah, in the Ten Commandments (Exodus 20:8-11 and Deuteronomy 5:12-15). Detailed laws are found in the Shulchan Aruch, Orach Chayim 242:1.
The laws of Kashrut (dietary laws) are derived from the Torah, primarily from Leviticus 11 and Deuteronomy 14. Detailed laws are codified in Yoreh De'ah 87:1.
The commandment to wear Tefillin is found in the Torah in four places: Exodus 13:1-10, Exodus 13:11-16, Deuteronomy 6:4-9, and Deuteronomy 11:13-21. Detailed laws are found in Shulchan Aruch, Orach Chayim 25:1.
The prohibition against Lashon Hara (negative speech) is based on various verses in the Torah, such as Leviticus 19:16. Detailed discussions can be found in the Chofetz Chaim, Introduction:1.
The laws of making a blessing before eating (Bracha Rishona) are found in the Talmud, Berakhot 35a. Codified laws are in Shulchan Aruch, Orach Chayim 206:1.
The requirement to say a blessing after eating (Bracha Acharona) is based on Deuteronomy 8:10. Detailed laws are in Shulchan Aruch, Orach Chayim 208:1.
"""

def main():
    st.title("Torah Sources Finder")
    st.write("Enter any topic, subject, halacha, or posek to find its source.")

    query = st.text_input("Enter your query:")
    if st.button("Find Source"):
        if query:
            result = nlp(question=query, context=context)
            if result and result['score'] > 0.1:
                st.success(f"Source: {result['answer']}")
            else:
                st.error("Source not found. Please try another query.")
        else:
            st.error("Please enter a query.")

if __name__ == "__main__":
    main()
