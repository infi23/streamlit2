import streamlit as st

def page_2():
    st.title('Page 2')
    st.write('Ini adalah konten untuk Page 2')
    # st.video("https://www.youtube.com/watch?v=2qcsb8n55Ds")
    st.video("https://www.youtube.com/watch?v=2qcsb8n55Ds", format='video/mp4', start_time=0)
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
    st.latex(r'''
    \[f'(x) = \mathop {\lim }\limits_{h \to 0} \,\,\frac{{f(x + h) - f(x)}}{h}\]
    ''')
