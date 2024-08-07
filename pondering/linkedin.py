url ='https://www.linkedin.com/in/xuhu-zhou-ba5483245/'

import streamlit as st

def app():
    st.subheader('COME TO SEE my linkin!')
    st.markdown(f'<a href="{url}" target="_blank" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px;">Donate</a>', unsafe_allow_html=True)
