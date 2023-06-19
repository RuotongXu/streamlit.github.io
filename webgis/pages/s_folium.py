#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:50:22 2023

@author: rt

"""
# 利用map()函数显示地图

import pandas as pd
import streamlit as st
st.title('长三角环境监测点分布图')
url_data = "https://EcnuGISChaser.github.io/gis_development/data/csj_pm25.csv"
df = pd.read_csv(url_data,usecols=["经度","纬度"],encoding="utf8")
df["lon"] = df["经度"]
df["lat"] = df["纬度"]
st.map(df)


# 构建一个ScatterplotLayer并显示

import streamlit as st
import pandas as pd
import pydeck as pdk
st.title("pydeck示例")
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

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd
#url = "https://ecnugischaser.github.io/gis_development/data/tms_POIs.geojson"
data = r'https://ecnugischaser.github.io/gis_development/data/tms_POIs.geojson'
st.write(data)
gdf = gpd.read_file(data)
config ={'version': 'v1',
         'config': {'mapStyle':{'styleType':'satellite'}}}
map_1 = KeplerGl(height=400,config=config)
map_1.add_data(gdf, 'china cities')
keplergl_static(map_1,center_map=True)

import folium
import streamlit as st
from streamlit_folium import st_folium

st.write("""
         # 在Streamlit app中显示folium构建的Map对象并返回地图操作信息
         """)

st.title("streamlit_folium示例")
tiles = 'http://webst01.is.autonavi.com/appmaptile?style=7&x={x}&y={y}&z={z}'
attr = '高德地图'
m = folium.Map(width = 600,height = 400,tiles=tiles,attr=attr,
               location=[30,115],zoom_start = 4)
cities=[
    ["北京",116.37,39.92,2170,"https://jpwu19860184.github.io/china/beijing.jpg"],
    ["上海",121.53,31.26,2418,"https://jpwu19860184.github.io/china/shanghai.jpg"],
    ["广州",113.25,23.13,1449,"https://jpwu19860184.github.io/china/guangzhou.jpg"] ]

for city in cities:
    city_name = city[0]
    x = city[1]
    y = city[2]
    pop = city[3]
    img_src = city[4]
    html = f"""<h4>{city_name}</h4>
               人口：{pop}万
               <img src={img_src}>
            """
    popup = folium.Popup(html,max_width=200)
    folium.Marker(location=[y,x],
                  popup=popup).add_to(m)
output = st_folium(m, width=700, height=500)
st.write("你点击位置的坐标是：")
st.write(output["last_clicked"])
st.write("目前的比例尺级别是：")
st.write(output["zoom"])


st.write("""
         # 在web应用中显示keplergl地图
         """)

from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd
#url = "https://ecnugischaser.github.io/gis_development/data/tms_POIs.geojson"
data = r'https://ecnugischaser.github.io/gis_development/data/tms_POIs.geojson'
st.write(data)
gdf = gpd.read_file(data)
config ={'version': 'v1',
         'config': {'mapStyle':{'styleType':'satellite'}}}
map_1 = KeplerGl(height=400,config=config)
map_1.add_data(gdf, 'china cities')
keplergl_static(map_1,center_map=True)
