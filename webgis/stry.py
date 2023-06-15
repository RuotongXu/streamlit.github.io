#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:57:11 2023

@author: rt
"""

import streamlit as st 
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

import streamlit as st
st.title('my web app:coffee:')
st.header('显示Markdown文本')
text = """
**Markdown**是一种文本格式的*标记语言*，能够使文本按照一定的格式进行显示。类似于:red[HTML]文档，但标签比:blue[HTML]简单。
"""
st.markdown(text)

import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
'''
输入的是dataframe
'''   
import pandas as pd
import streamlit as st

data = [[116.37,39.92,2170],[121.53,31.26,2418],
        [113.25,23.13,1449]]
frame = pd.DataFrame(data,index=["北京","上海","广州"],
                     columns=["经度","纬度","人口"])
st.dataframe(frame) 

'''
输入的是字典
'''

import streamlit as st

data = {"城市名":["北京","上海","广州"],
       "人口":[2170,2418,1449],
       "经度":[116.37,121.53,113.25],
       "纬度":[39.92,31.26,23.13]
}
st.dataframe(data) 

'''
读取远程的csv数据并以dataframe形式显示
'''

import pandas as pd
import streamlit as st
st.title('长三角PM2.5监测数据')
url_data = "https://EcnuGISChaser.github.io/gis_development/data/csj_pm25.csv"
df = pd.read_csv(url_data,encoding="utf8")
st.dataframe(df) 


'''
以metric形式显示数据
'''
import streamlit as st

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

# 以pretty-printed JSON格式显示json字符串（可以对每个节点进行展开或收缩）

import streamlit as st

cities = {'Beijing': {'coord': {'lat': 39.92, 'lon': 116.37}, 'pop': 2170},
 'Guangzhou': {'coord': {'lat': 23.13, 'lon': 113.25}, 'pop': 1449},
 'Shanghai': {'coord': {'lat': 31.26, 'lon': 121.53}, 'pop': 2418}}

st.json(cities)

# 利用line_chart()函数绘制线图

import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 利用pyplot()函数绘制matplotlib图表

import streamlit as st
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar([1,2,3],[87,65,34],width=0.5,color="r")
ax.bar([1.5,2.5,3.5],[93,74,50],width=0.5,color="b")
st.pyplot(fig)

# 绘制长三角城市PM2.5监测数据曲线图（前5个城市）

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.title('长三角城市PM2.5监测数据曲线图')
#plt.rcParams["font.family"] = "SimHei"
#plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['font.family'] = ['Arial Unicode MS']
fig, ax = plt.subplots()
url_data = "https://EcnuGISChaser.github.io/gis_development/data/csj_pm25.csv"
df = pd.read_csv(url_data,encoding="utf8")
city_df = df.drop(["经度","纬度"],axis=1).groupby("城市").mean().round(2)
for i in range(5):
    y = list(city_df.iloc[i])
    ax.plot(y,label=city_df.iloc[i].name)
plt.xlabel("月份")
plt.ylabel("PM2.5")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],
           ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"])
plt.legend(loc=3)
st.pyplot(fig)

# 利用plotly_chart()函数绘制图表

import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

# 构建一个ScatterplotLayer并显示

import streamlit as st
import pandas as pd
import pydeck as pdk
data = [[39.92,116.37],[31.26,121.53],[23.13,113.25]]
chart_data = pd.DataFrame(data,columns=['lat','lon'])
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=31.26,
        longitude=121.53,
        zoom=11,
        pitch=50),
    layers=[
      pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[255, 0, 0, 255]',
            get_radius=50000)],
))

# 利用map()函数显示地图

import pandas as pd
import streamlit as st
st.title('长三角环境监测点分布图')
url_data = "https://EcnuGISChaser.github.io/gis_development/data/csj_pm25.csv"
df = pd.read_csv(url_data,usecols=["经度","纬度"],encoding="utf8")
df["lon"] = df["经度"]
df["lat"] = df["纬度"]
st.map(df)



#df = pd. read _csv ("my_data. csv")
#st.line_chart (df)