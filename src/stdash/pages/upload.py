import streamlit as st
import pandas as pd
from io import StringIO
import requests
import json

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

def load_data():
    if uploaded_file is not None:
    
        headers = {
        'accept': 'application/json',
        }

        files = {
            'file': uploaded_file.getvalue()
        }

        response = requests.post('http://127.0.0.1:8000/uploadfile/', headers=headers, files=files)
    
        if response.status_code == 200:
            data = response.json()

            if data['label'] == 'hot dog':
                st.write('hot dog')
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxqqIG2n685k1AS3HyuhXLgMsySGTozbxNvQ&s")

            else:
                st.write('not hot dog')
                st.image("https://mblogthumb-phinf.pstatic.net/MjAyMjAyMDdfMjEy/MDAxNjQ0MTk0Mzk2MzY3.WAeeVCu2V3vqEz_98aWMOjK2RUKI_yHYbuZxrokf-0Ug.sV3LNWlROCJTkeS14PMu2UBl5zTkwK70aKX8B1w2oKQg.JPEG.41minit/1643900851960.jpg?type=w800")

load_data()
