import streamlit as st
from page1 import page_1  # Import fungsi page_2 dari file page2.py
from page2 import page_2  # Import fungsi page_2 dari file page2.py
from page3 import page_3  # Import fungsi page_2 dari file page2.py
from page4 import page_4  # Import fungsi page_2 dari file page2.py

PAGES = {
    "Page 1": page_1,
    "Page 2": page_2,
    "Page 3": page_3,
    "Page 4": page_4,
}

# Sidebar
st.sidebar.image("logo.png", width=100)  # Ganti "logo.png" dengan path file logo Anda
page = st.sidebar.radio("Pilih Halaman", list(PAGES.keys()))

# Konten Utama
PAGES[page]()
