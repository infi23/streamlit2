import streamlit as st
import base64
import os


# Fungsi untuk menampilkan halaman PDF
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    # Embedding PDF in HTML
    pdf_display = f"""<embed
    class="pdfobject"
    type="application/pdf"
    title="Embedded PDF"
    src="data:application/pdf;base64,{base64_pdf}"
    style="overflow: auto; width: 100%; height: 100vh; max-width: 100%; max-height: 100%;">"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


def page_4():
    st.title("PDF Viewer")
    current_directory = os.getcwd()
    sub_directory = "filex"
    file_directory = os.path.join(current_directory, sub_directory)
    # st.write("Direktori kerja saat ini:", file_directory)
    pdf_files = [f for f in os.listdir(file_directory) if f.endswith(".pdf")]
    # pdf_files = [os.path.join(file_directory, f) for f in os.listdir(file_directory) if f.endswith(".pdf")]
    selected_file = st.selectbox("Pilih file PDF", pdf_files)
    # st.write(pdf_files)
    # Tampilkan halaman PDF yang dipilih
    if selected_file:
        displayPDF(os.path.join(file_directory, selected_file))


# if __name__ == "__main__":
#     main()
