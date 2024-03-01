# import streamlit as st

# # Sidebar
# st.sidebar.image("logo.png")  # Ganti "logo.png" dengan path file logo Anda
# st.sidebar.button('Page 1')
# st.sidebar.button('Page 2')
# st.sidebar.button('Page 3')
# st.sidebar.checkbox('Checkbox 01')
# st.sidebar.checkbox('Checkbox 02')
# st.sidebar.selectbox('ComboBox', ['Option1', 'Option2', 'Option3'])

# # Konten Utama
# st.title('My_app_name')
# st.write('Deskripsi aplikasi Anda di sini')

# # Membuat grafik (ganti dengan data Anda)
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Grafik Contoh')

# st.pyplot(fig)

# if st.button('Download Chart Data'):
#     st.write('Fungsi unduh belum diimplementasikan')
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def page_1():
    st.title('Page 1')
    st.write('Deskripsi aplikasi Anda di sini')

    # Membuat grafik (ganti dengan data Anda)
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Grafik Contoh')

    st.pyplot(fig)

    if st.button('Download Chart Data'):
        st.write('Fungsi unduh belum diimplementasikan')

def page_2():
    st.title('Page 2')
    st.write('Ini adalah konten untuk Page 2')

def page_3():
    st.title('Page 3')
    st.write('Ini adalah konten untuk Page 3')

PAGES = {
    "Page 1": page_1,
    "Page 2": page_2,
    "Page 3": page_3
}

# Sidebar
st.sidebar.image("logo.png")  # Ganti "logo.png" dengan path file logo Anda
page = st.sidebar.radio("Pilih Halaman", list(PAGES.keys()))
st.sidebar.checkbox('Checkbox 01')
st.sidebar.checkbox('Checkbox 02')
st.sidebar.selectbox('ComboBox', ['Option1', 'Option2', 'Option3'])

# Konten Utama
PAGES[page]()
