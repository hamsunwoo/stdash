import streamlit as st
import os

os.environ['LC_ALL'] = 'C'

st.set_page_config(page_title="Insight", page_icon="📈")

st.markdown("# Insight")
st.sidebar.header("Insight")
st.image('https://i.lgtm.fun/2tw5.png')
st.write(
    """- 2024년 9월 25일에 가장 많은 요청
    """)
st.write(
    """
        - n77 요청자의 처리가 1분을 초과
    """)
