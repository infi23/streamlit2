import streamlit as st

def page_1():
    st.title('Page 1')
    st.write('Ini adalah konten untuk Page 1')
    with open("halo.md", "r") as file:
        markdown_text = file.read()

    # Tampilkan konten Markdown di aplikasi Streamlit
    st.markdown(markdown_text)
