import pandas as pd
import matplotlib.pyplot as plt
import requests
import streamlit as st

st.title('Requests by Date and Time')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

# TODO
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
df['request_time'] = pd.to_datetime(df['request_time'])
df['request_hour'] = df['request_time'].dt.strftime('%Y-%m-%d %H')
# 즉 시간별 GROUPBY COUNT 하여 plt 차트 그려보기
df1 = df.groupby(df['request_hour']).count()
df1['request_hour'] = df1.index

plt.bar(df1['request_hour'], df1['num'])
plt.plot(df1['request_hour'], df1['num'], 'ro-')
plt.xlabel('request_time')
plt.ylabel('Number of Requests')
plt.xticks(rotation=45,fontsize=10)
plt.tight_layout()

st.pyplot(plt)
