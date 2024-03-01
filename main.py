import streamlit as st
from page1 import page_1  # Import fungsi page_2 dari file page2.py
from page2 import page_2  # Import fungsi page_2 dari file page2.py
from page3 import page_3  # Import fungsi page_2 dari file page2.py
from page4 import page_4  # Import fungsi page_2 dari file page2.py

# Definisikan fungsi untuk halaman pertama (page_1) dan halaman ketiga (page_3) di sini

# Fungsi untuk halaman pertama
# def page_1():
#     st.title('Page 1')
#     st.write('Deskripsi aplikasi Anda di sini')


# Fungsi untuk halaman ketiga

PAGES = {
    "Page 1": page_1,
    "Page 2": page_2,
    "Page 3": page_3,
    "Page 4": page_4,
}

# Sidebar
st.sidebar.image("logo.png", width=100)  # Ganti "logo.png" dengan path file logo Anda
page = st.sidebar.radio("Pilih Halaman", list(PAGES.keys()))
# st.sidebar.checkbox("Checkbox 01")
# st.sidebar.checkbox("Checkbox 02")
# st.sidebar.selectbox("ComboBox", ["Option1", "Option2", "Option3"])

# Konten Utama
PAGES[page]()
