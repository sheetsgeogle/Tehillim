import streamlit as st
from transformers import pipeline

# Load a pre-trained question-answering model
nlp = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def main():
    st.title("Torah Sources Finder")
    st.write("Enter any topic, subject, halacha, or posek to find its source.")

    query = st.text_input("Enter your query:")
    context = st.text_area("Provide context (optional):", height=200)

    if st.button("Find Source"):
        if query:
            if not context:
                st.error("Please provide some context to search within.")
            else:
                result = nlp(question=query, context=context)
                if result and result['score'] > 0.1:
                    st.success(f"Source: {result['answer']}")
                else:
                    st.error("Source not found. Please try another query.")
        else:
            st.error("Please enter a query.")

if __name__ == "__main__":
    main()
