#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:36:02 2023

@author: rt
"""

import streamlit as st 
import pandas as pd

st.write("""
# 舌尖上的中国:flag-cn:之闽清三宝:sparkles:
##### 介绍人：许若橦:monkey:
\n
***
    """)

text = """
###### · 闽清县，简称“梅”，福州市辖县，位于福建省东部、闽江中下游，总面积1494平方千米，辖11个镇和5个乡。
 · 五代后梁乾化元年（911年）置县，涌现出宋代八闽第一位状元:blue[许将]，并称“梅溪二陈先生”的理学家:blue[陈祥道]、音乐家:blue[陈旸]两兄弟，集诗人、书画家、道教南宗五祖于一身的:blue[白玉蟾]，近代爱国侨领:blue[黄乃裳]，当代著名肝胆专家、中科院院士、国家最高科学技术奖得主:blue[吴孟超]等名人志士。
###### · 闽清三宝为：:green[橄榄]，:green[糟菜]，:green[茶口粉干]。以下将进行简单介绍。
\n
***
"""

st.markdown(text)



import folium
from streamlit_folium import st_folium


tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
attr = 'arcgisonline全球影像'


#
import geopandas as gpd
url = "https://ruotongxu.github.io/streamlit.github.io/minqing.geojson“
gdf = gpd.read_file(url, driver='GeoJSON')

m = folium.Map(width=800, height=600,tiles=tiles,attr=attr,
               location=[26.23273201141355,118.73807846069200],zoom_start = 11)

from folium import FeatureGroup
layer = FeatureGroup(name='POI', control=True)

folium.TileLayer( tiles="http://webst01.is.autonavi.com/appmaptile?style=8&x={x}&y={y}&z={z}",
    name="高德地图",attr="高德地图").add_to(m)

for i in range(len(gdf)):
    # 在地图上添加Marker对象
    lat = gdf['geometry'][i].y
    lon = gdf['geometry'][i].x
    name = gdf.iloc[i]['NAME']
    text = gdf.iloc[i]['text']
    #photo_url = gdf.iloc[i]['photo_url']
    html = f"""<h4>{name}</h4>
               <h6>{text}</h6>
               
            """
    #<img src={photo_url}>
    popup = folium.Popup(html,max_width=200)
    marker = folium.Marker(location = (lat, lon), popup=popup)
    marker.add_to(layer)

layer.add_to(m)

output = st_folium(m, width=800, height=600)

# ,opacity=0.6
from PIL import Image

'''
image1 = Image.open(r'/Users/rt/Downloads/橄榄（青.jpg')
#image2 = Image.open(r'C:\data\photos\p2.jpg')
#image3 = Image.open(r'C:\data\photos\p3.jpg')
st.image(image1)
'''

text = """
### 橄榄
史书早有“味虽苦涩，咀之芳馥，胜含鸡骨”的记载。受温度、湿度制约，只适宜于我国东南沿海热带、亚热带薄霜气候区种植的橄榄，在闽清已有近千年的人工栽培历史，并呈区域、规模发展的态势。
主要品种有：檀香、惠园、自来园、长营等，其中以鲜食为主的檀香橄榄为果中极品。其果小而圆，肉厚而质脆，始偿稍带苦涩，嚼后清香甘甜，回味绵长。自唐代以来，被列为贡品。
闽清的芳雨天源橄榄种植规模已达4万亩，年产量5000吨。随着投产面积的扩大，其产量将逐年递增。
"""

st.markdown(text)

text = """
### 糟菜
闽清糟菜风味独特，其味甘酸香醇，有去腥腻、增食欲、开胃清津之功效。明朝郑和下西洋时，曾将闽清糟菜随船带往海外，随后即源源不断地出口东南亚各国。闽清糟菜色香味俱全。相传为白岩山猴所创，后经人们的不断改进，制作工艺日臻完备，为闽清所独有。“上排煮糟菜”这道平常百姓餐桌上的菜肴，令胡耀邦、李鹏等党和国家领导人赞不绝口。闽清家家种芥菜，户户腌糟菜。全县芥菜种植面积12万多亩，年产糟菜1500吨，产品打入美国、日本、东南亚等国示市场。特别是近年来兴起的小包装糟菜，经过深度加工，以方便、即食、可口的特性，成为馈赠亲友的精品。
"""

st.markdown(text)

text = """
### 茶口粉干
茶口为梅溪源头的一个村落。因村之井水清香可口，像溶进了香茶，故得名“茶口”。茶口村生产粉干已有800多年的历史。因水质好、做工细、选料精良，采用自然风干等办法，所产粉干洁白匀长、细润柔韧，且久煮不烂、翻炒不粘不碎，日久天长而闻名遐迩，被列入《中国食品大全》。随着制作工艺和制作规程的改进，茶口粉干的品质、口感日益变好。特别是闽清茶口粉干厂大胆推进制作工艺和制作规程创新，使茶口粉干的生产突破依靠自然风干的这道工序约束，改为机械烘干后，产量成倍增长。茶口粉干年产能力达3000吨，产品畅销海内外。
"""

st.markdown(text)
