import streamlit as st
from transformers import pipeline

# Load a pre-trained model and tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
nlp = pipeline("question-answering", model=model_name)

# Predefined context simulating Torah sources
context = """
Shabbat: Shulchan Aruch, Orach Chayim 242:1.
Kashrut: Yoreh De'ah 87:1.
Tefillin: Shulchan Aruch, Orach Chayim 25:1.
Lashon Hara: Chofetz Chaim, Introduction:1.
Bracha Rishona: Shulchan Aruch, Orach Chayim 206:1.
Bracha Acharona: Shulchan Aruch, Orach Chayim 208:1.
"""

def main():
    st.title("Torah Sources Finder")
    st.write("Enter any topic, subject, halacha, or posek to find its source.")

    query = st.text_input("Enter your query:")
    if st.button("Find Source"):
        if query:
            result = nlp(question=query, context=context)
            st.success(f"Source: {result['answer']}")
        else:
            st.error("Please enter a query.")

if __name__ == "__main__":
    main()
