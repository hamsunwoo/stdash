import streamlit as st
import os

os.environ['LC_ALL'] = 'C'

st.set_page_config(page_title="About me", page_icon="📈")

st.markdown("# About me")
st.sidebar.header("About me")
st.write(
    """### Email: summerham22@gmail.com
    """)
st.write(
    """
    ### Github: https://github.com/hamsunwoo
    """)
st.image('https://i.lgtm.fun/2swy.png')
