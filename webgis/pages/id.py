#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:21:05 2023

@author: rt
"""

import streamlit as st
import requests
st.title('身份证号解析')
url = "https://api.asilu.com/idcard/?"
in_txt = st.text_input('请输入身份证号')#,value="152502199405148245")
parameters = f"id={in_txt}"
st.button("确定")
try:
    response = requests.get(url + parameters)
    dic = response.json()
    out_txt = f"""地址：{dic['addr']}
出生日期：{dic['date']}
性别：{dic['sex']}
"""
    st.text_area('解析结果',value=out_txt)
except:
    st.write("身份证号有误")

'''
import streamlit as st
txt = st.text_input('请输入密码',value="",type="password")
st.button("确定")
if txt!="":
    if txt=="abc":
        st.write("your password is right!")
    else:
        st.write("your password is wrong!")
'''

# 通过交互方式返回地图切片
import streamlit as st
from math import log,tan,pi
import requests

st.title("返回地图切片")
z = st.number_input('输入比例尺级别0~18',min_value=0,max_value=18,value=0,format="%d")
lng = st.number_input('输入经度-180~180',min_value=-180.,max_value=180.,value=0.,format="%f")
lat = st.number_input('输入纬度-90~90',min_value=-90.,max_value=90.,value=0.,format="%f")
st.button('确定')
r = 20037508.34
x = lng*r/180 
y = log(tan(pi/4+lat*pi/360))*(r/pi)  
d = 40075014/(2**int(z))
row = int((20037507-y)/d)
col = int((x-(-20037507))/d)
url = f"https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{row}/{col}.png"
response = requests.get(url)
image = response.content   
st.image(image, width = 400,caption=f'z={z},lng={lng},lat={lat}')
