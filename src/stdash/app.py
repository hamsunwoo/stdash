import pandas as pd
import matplotlib.pyplot as plt
import requests
import streamlit as st
import os

t1, t2 = st.tabs(['Requests by Date and Time', '불균형요청수'])

#st.title('Requests by Date and Time')

def load_data():
    DB = os.getenv('DB')
    DB_PORT = os.getenv('DB_PORT')
    url = f'http://{DB}:{DB_PORT}/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

# TODO
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
with t1:
    df['request_time'] = pd.to_datetime(df['request_time'])
    df['prediction_time'] = pd.to_datetime(df['prediction_time'])

    df['request_hour'] = df['request_time'].dt.strftime('%Y-%m-%d %H')
    df['prediction_hour'] = df['prediction_time'].dt.strftime('%Y-%m-%d %H')

    df1 = df.groupby(df['request_hour']).count()
    df2 = df.groupby(df['prediction_hour']).count()
    df1['request_hour'] = df1.index
    df2['prediction_hour'] = df2.index

    plt.bar(df1['request_hour'], df1['num'])
    plt.plot(df2['prediction_hour'], df2['num'], 'ro-')
    plt.title('Requests by Date and Time')
    plt.xlabel('request_time')
    plt.ylabel('Number of Requests')
    plt.xticks(rotation=45,fontsize=10)
    plt.tight_layout()

    st.pyplot(plt)

#불균형(누가 처리에 문제가 있는지 확인) VIEW 추가
with t2:
    plt.figure() #새로운 그래프를 그림
    df['request_day'] = df['request_time'].dt.strftime('%Y-%m-%d')
    df['request_h'] = df['request_time'].dt.hour
    df['request_minute'] = df['request_time'].dt.minute

    df['predict_day'] = df['prediction_time'].dt.strftime('%Y-%m-%d')
    df['predict_h'] = df['prediction_time'].dt.hour
    df['predict_minute'] = df['prediction_time'].dt.minute

    df['hour_difference'] = df['predict_h'] - df['request_h']
    df['minute_difference'] = df['predict_minute'] - df['request_minute']
    filtered_df = df[(df['minute_difference'] > 1) | (df['hour_difference'] < 0) | (df['hour_difference'] > 0) | (df['minute_difference'] < 1)]

    df3 = filtered_df.groupby(filtered_df['request_user']).count()
    df3['request_user'] = df3.index

    plt.bar(df3['request_user'].index, df3['minute_difference'], color='blue')
    bar = plt.bar(df3['request_user'].index, df3['minute_difference'])
    
    # 값 넣는 부분
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 12)

    plt.title('unbalanced requests counting')
    plt.xlabel('request_user')
    plt.ylabel('count')
    plt.xticks(rotation=45,fontsize=10)
    plt.tight_layout()

    st.pyplot(plt)
