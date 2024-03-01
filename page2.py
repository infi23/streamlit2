import streamlit as st

def page_2():
    st.title('Page 2')
    st.write('Ini adalah konten untuk Page 2')
    # st.video("https://www.youtube.com/watch?v=2qcsb8n55Ds")
    st.video("https://www.youtube.com/watch?v=PrwSPTDqf_o")

    st.write('Rumus Umum Turunan Fungsi')    
    st.latex(r'''
    f'(x) = \mathop {\lim }\limits_{h \to 0} \,\,\frac{{f(x + h) - f(x)}}{h}
    ''')
