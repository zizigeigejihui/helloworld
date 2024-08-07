import streamlit as st
from datetime import time, datetime
# 192.168.3.38

#测试能否远程连接mysql数据库
import pymysql
try:
    conn = pymysql.connect(host='192.168.3.38', user='root', password='18921190757ytk', db='zion', charset='utf8')
    print(conn)
    st.write("连接成功")
except Exception as e:
    print(e)
    print("连接失败")
    #关闭连接
    conn.close()

st.header('st.slider')

# 样例 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 样例 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 样例 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 样例 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)