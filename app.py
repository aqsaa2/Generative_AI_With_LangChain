import streamlit as st_size
import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain



def main():
    st.set_page_config("Business Analyst AI Agent")
    st.header("Generative AI With LangChain")

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the Submit & Process button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)

                


                time.sleep(2)
                st.success("Done")


if __name__ == "__main__":
    main()