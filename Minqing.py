#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:36:02 2023

@author: rt
"""

import streamlit as st 
import pandas as pd

st.write("""
# 闽清县志:computer:
###### 感谢访问！
###### 借助互联网，一起来了解更加丰满立体的我的家乡——闽清县吧！
##### 制作人：许若橦:monkey:
\n
***
    """)

text = """
###### · 闽清县，简称“梅”，福州市辖县，位于福建省东部、闽江中下游，总面积1494平方千米，辖11个镇和5个乡。
 · 五代后梁乾化元年（911年）置县，涌现出宋代八闽第一位状元:blue[许将]，并称“梅溪二陈先生”的理学家:blue[陈祥道]、音乐家:blue[陈旸]两兄弟，集诗人、书画家、道教南宗五祖于一身的:blue[白玉蟾]，近代爱国侨领:blue[黄乃裳]，当代著名肝胆专家、中科院院士、国家最高科学技术奖得主:blue[吴孟超]等名人志士。
\n
***
"""

st.markdown(text)












st.write("""
         ### 闽清三宝
         闽清三宝为：:green[橄榄]，:green[糟菜]，:green[茶口粉干]。以下将进行简单介绍。
         """)
         
import requests

url = f"https://ruotongxu.github.io/streamlit.github.io/photos/sanbao.jpg"
response = requests.get(url)
image = response.content   
st.image(image, width = 200,caption='闽清三宝')



text = """
#### 橄榄
史书早有“味虽苦涩，咀之芳馥，胜含鸡骨”的记载。受温度、湿度制约，只适宜于我国东南沿海热带、亚热带薄霜气候区种植的橄榄，在闽清已有近千年的人工栽培历史，并呈区域、规模发展的态势。
主要品种有：檀香、惠园、自来园、长营等，其中以鲜食为主的檀香橄榄为果中极品。其果小而圆，肉厚而质脆，始偿稍带苦涩，嚼后清香甘甜，回味绵长。自唐代以来，被列为贡品。
闽清的芳雨天源橄榄种植规模已达4万亩，年产量5000吨。随着投产面积的扩大，其产量将逐年递增。
##### 三宝趣闻：檀香橄榄
据《闽清县志》载：从前，本县有个叫池香的老人，常往返南洋做生意。当时南洋已有不少闽清籍华侨。他每次出洋，总有许多人托他带话、捎信给海外亲友，因此很受侨胞欢迎和尊重。有一回，池香从南洋返航，许多侨胞难分难舍地送他上船，对他说：“我们离乡久了，真想尝尝家乡风味，下回你能不能给我们带点吃的东西？”他爽快地答应了。一路上，池香想起自己的承诺，可犯愁了。他一直揣摩：“南洋乡亲少说也有大几千人，带什么东西才能经久不坏，又能够那么多人分享呢？”经过两三个月的海上颠簸，池香回到闽清正是橄榄收成季节。见满树满园的橄榄，他心头一亮，买了几担小粒的橄榄，特制几个大桶，用橄榄叶铺垫好，然后倒进橄榄，包装严密，以防海水侵蚀。三个月后，池香又到了南洋。侨胞闻讯赶来探问。他边应酬边从船舱搬出木桶，撬开桶盖，顿时芬芳四溢。只见橄榄颗颗碧绿油亮，放进嘴里嚼，清甜脆嫩，口齿留香。就这样一人一颗，嚼得津津有味。大家问这橄榄的名称，池香笑着说：“叫‘小粒橄榄’，真是有损其身价，你们替它起个芳名吧。”有个侨胞说：“别看小粒，比这里的檀香木还要香哩。”于是“檀香橄榄”就这样叫开了。
"""
st.markdown(text)

col2, col3 = st.columns(2)

url = f"https://ruotongxu.github.io/streamlit.github.io/photos/qingganlan.jpg"
response = requests.get(url)
image = response.content   
col2.image(image, width = 400,caption='青橄榄')
url = f"https://ruotongxu.github.io/streamlit.github.io/photos/yanganlan.jpg"
response = requests.get(url)
image = response.content   
col3.image(image, width = 400,caption='腌制橄榄')



text = """
#### 糟菜
闽清糟菜风味独特，其味甘酸香醇，有去腥腻、增食欲、开胃清津之功效。明朝郑和下西洋时，曾将闽清糟菜随船带往海外，随后即源源不断地出口东南亚各国。闽清糟菜色香味俱全。相传为白岩山猴所创，后经人们的不断改进，制作工艺日臻完备，为闽清所独有。“上排煮糟菜”这道平常百姓餐桌上的菜肴，令胡耀邦、李鹏等党和国家领导人赞不绝口。闽清家家种芥菜，户户腌糟菜。全县芥菜种植面积12万多亩，年产糟菜1500吨，产品打入美国、日本、东南亚等国示市场。特别是近年来兴起的小包装糟菜，经过深度加工，以方便、即食、可口的特性，成为馈赠亲友的精品。
##### 三宝趣闻：闽清糟菜
民间流传着这样的故事：闽清六都附近白岩山，山高林密，沟深洞多，三五十里方圆古木参天，荫翳蔽日，野兽多，猴子也多。庄稼菜园常受糟蹋，人畜不得安宁。农家为防兽驱兽，人人都会打猎捕兽，自制扒拨箭、绊兽索、张猫机等诱捕野兽。一天，有个农民在菜园中安张猫机，本来想逮野猫山兔，谁想把猴子套上了。猴子吱吱乱叫，当农民赶到时猴子已挣脱逃跑。猴子见人赶来，便起报复心。当天晚上招来群猴，把这菜园的萝卜、芥菜拔个精光。一时吃不完，就放在悬崖顶上晾晒，晒干后，用带咸酸味的树汁和泥搓软，腌藏在砍断的毛竹里，表面用黄泥封紧，乱草遮密。不久，毛竹里的腌菜被人家发现了，人们尝到别有风味的“酸甜菜”，赞不绝口。这事传开了，大家深受启发，加工出更香甜可口的腌菜：将鲜嫩芥菜晒干，用酒糟和食盐抹菜搓软装入瓮中挤压紧密，再用黄土密封瓮口，再将瓮翻倒扣盖在草木灰上，半年后取出，就是芳香扑鼻、脍炙人口的腌菜了。因主要用红糟腌，故俗称“糟菜”。1982年11月4日，中共中央总书记胡耀邦到闽清视察农村小水电，吃到糟菜炖上排，赞不绝口，对随行项南书记说：这糟菜不错，外观朴素，内质美味，可以作为一个地方土特产规模开发嘛！从此，闽清糟菜闻名遐迩，这些年还远销欧美呢！
"""

st.markdown(text)
url = f"https://ruotongxu.github.io/streamlit.github.io/photos/zaocai.jpg"
response = requests.get(url)
image = response.content   
st.image(image, width = 200,caption='糟菜')


text = """
#### 茶口粉干
茶口为梅溪源头的一个村落。因村之井水清香可口，像溶进了香茶，故得名“茶口”。茶口村生产粉干已有800多年的历史。因水质好、做工细、选料精良，采用自然风干等办法，所产粉干洁白匀长、细润柔韧，且久煮不烂、翻炒不粘不碎，日久天长而闻名遐迩，被列入《中国食品大全》。随着制作工艺和制作规程的改进，茶口粉干的品质、口感日益变好。特别是闽清茶口粉干厂大胆推进制作工艺和制作规程创新，使茶口粉干的生产突破依靠自然风干的这道工序约束，改为机械烘干后，产量成倍增长。茶口粉干年产能力达3000吨，产品畅销海内外。
##### 三宝趣闻：茶口粉干
传说很久以前，闽清五都（今塔庄镇）茶口村有个财主，讨了三妻四妾，丫环成群，过着花天酒地的生活。家人每天吃不完的饭都倒进房前的一条小溪。小溪下游有个穷苦的村民，见到白花花的米饭被水冲走，十分心疼，用竹筐把米饭打捞起来搓成米团晒干藏在缸里，青黄不接时拿出来用水煮后切成片，下锅煮了吃。一天当厨师的亲戚到他家，村民就用“米干片”请客，客人觉得新奇，便问起来，他吃后觉得比大米饭好吃，想加工一种大米做的点心，扩大生意门路。于是，他选好米磨成浆，压成粉团，搓成粿，用井水煮，挤压成粉丝，晒干就成“粉干”了。相传郑和下西洋时曾带粉干销往南洋，受到海外人士的赞赏，以后华侨探亲常捎带粉干，“粉干”便名扬四海了。奇怪的是闽清县惟有这个村加工制作的“粉干”，质量上乘口感好，外观雅致，因此，“茶口粉干”成了闽清粉干的精品，特别畅销。
"""

st.markdown(text)
url = f"https://ruotongxu.github.io/streamlit.github.io/photos/粉干.jpg"
response = requests.get(url)
image = response.content   
st.image(image, width = 200,caption='粉干（生）')

st.write("""
         ***
         ### “瓷都"闽清
         """)
text = """
高岭土(瓷土) 为县内蕴藏量最大的矿产资源，主要分布在池园、白中、白樟、上莲、佳头，还有东桥、省璜、雄江等地。经省地质五队、省冶金厅地质队、省区划测量队和县地质部门1961、1981和1982年勘察，为风化热液型，预测储藏量达1680.75万吨，加上未探明的十多个矿点，总储量在2000万吨以上，其中储藏量在百万吨以上的有珠中、后寨、福斗、白汀、上宝山等矿点，不仅数量多，且质量好。
\n闽清是陶瓷之乡，迄今已有800多年历史。陶瓷生产历史可追溯到南宋年间，以电陶、建陶为主要产品的陶瓷产业长期是闽清支柱产业。改革开放40年来，闽清陶瓷业经过改革、改制、内联外引，使得全县55条现代化建陶生产线，主要设备引进技术占70%以上，以豪业陶瓷等领先的规上企业，生产出与世界媲美的三大系列、一千多个品种的陶质、瓷质砖。2017年，闽清县陶瓷出口总额达到3.5亿元，现已成为中国陶瓷生产基地县。
"""


st.markdown(text)


st.write("""
         ***
         ### 全国最大单体古民居——宏琳厝
         """)

text = """
“厝”在福福建闽东方言中，是老房子的意思。
\n建省闽清县坂东镇新壶村，有一座规模庞大的古民居——宏琳厝（俗称新壶里）。它历经几个世纪的风雨沧桑仍然屹立，以独特和鲜明的时代特征凸显在人们的面前。宏琳厝是全国最大的、保存最完好的古民居单体建筑。
\n宏琳厝由始祖药材商人黄作宾于清乾隆乙卯六十年（公元1795）始建，至其子宏琳1823年方全部落成，前后历时28年。宏琳厝占地面积17832.28平方米，共有大小厅堂35间、住房666间、花圃25个、天井30个、水井4口，厝内廊回路转，纵横有序，建筑为土木结构，对称翼券仰，雕梁画栋，是一座一次性设计、一气呵成、整体结构精巧的民居建筑。老宅已沐风雨二百年，厝内子孙繁衍十一代，人口两千多人，遍布海内外。
"""


st.markdown(text)


st.write("""
         ***
         ### 温泉之都
         """)

text = """
七叠温泉景区位于闽清县塔庄镇斜洋村，是国家3A级景区。景区四面环山，林木葱郁，空气清新，风景秀丽，是集洗浴健身、休闲娱乐、餐饮住宿、会议接待、农业观光为一体的综合性温泉旅游度假胜地。此地温泉出水口海拔 400余米，是福建省内已开发的海拔最高的温泉。
\n黄楮林温泉景区素有“中国温泉第一溪”之称，现为四星级乡村旅游经营单位。地处国家级黄楮林自然保护区内，位于福建省闽清县雄江镇，距福州市区约90千米。
黄楮林登山景区，内有丰富的森林资源和原生态的自然植被，其间遍布世界稀有、中国分布面积最大的珍贵的树种——黄楮林，并有近二十种国家级保护动植物。景区属低山丘陵貌，沟谷纵横，峰峦叠嶂，流泉飞瀑，富含负氧离子，是天然氧吧。
"""


st.markdown(text)


from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd
data = r'https://ruotongxu.github.io/streamlit.github.io/minqing.geojson'
gdf = gpd.read_file(data)
config ={'version': 'v2',
         'config': {
                    'legend':{'show': True, 'type': 'gradient'},
                    'mapState': {'latitude': 26.23273201141355,
                                 'longitude': 118.73807846069200,
                                 'zoom': 10}
                    }}
#'mapStyle': {'styleType':'satellite'},
map_1 = KeplerGl(height=800,config=config)
map_1.add_data(gdf, '介绍中提到的地点')




map_1.config = config
keplergl_static(map_1,center_map=True)








