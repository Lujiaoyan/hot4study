'''主页'''
import streamlit as st
page = st.sidebar.radio('首页',['兴趣推荐','图片处理工具','智慧词典','留言区','音乐'])
def page1():
    '兴趣推荐'
    st.write('兴趣推荐')
    st.write('-------------------------------------------------')
    st.write('难忘的北京之旅')
    st.write('-------------------------------------------------')
    st.write('长城')
    st.image('长城.jpg')
    st.write('-------------------------------------------------')
    st.write('天安门')
    st.image('天安门.jpeg')
    st.write('-------------------------------------------------')
    st.write('十七孔桥')
    st.image('十七孔桥.jpg')
    st.write('-------------------------------------------------')
    st.write('北京天文馆')
    st.image('北京天文馆.png')
    st.write('-------------------------------------------------')
    st.write('北京科技馆')
    st.image('北京科技馆.jpeg')
    st.write('-------------------------------------------------')
    st.write('北京大学')
    st.image('北京大学.png')
    st.write('-------------------------------------------------')
    st.write('故宫')
    st.image('123456.png')
    st.write('-------------------------------------------------')
def page2():
    '图片处理工具'
    st.write('图片处理工具')
def page3():
    '智慧词典'
    st.write('智慧词典')
def page4():
    '留言区'
    st.write('留言区')
def page5():
    '音乐'
    # st.write('音乐')
    # st.write('-------------------------------------------------')
    # st.write('Hillsong Young And Free-Wake.flac')
    # with open('Hillsong Young And Free-Wake.flac','rb') as f:
    #     mymp3 = f.read()
    # st.audio(mymp3,format='flac',start_time=0)
    # st.write('-------------------------------------------------')
    # st.write('某科学的超电磁炮 - only my railgun.mp3')
    # with open('某科学的超电磁炮 - only my railgun.mp3','rb') as f:
    #     mymp2 = f.read()
    # st.audio(mymp2,format='audio/mp3',start_time=0)
    # st.write('-------------------------------------------------')
if page == '兴趣推荐':
    page1()
elif page == '图片处理工具':
    page2()
elif page == '智慧词典':
    page3()
elif page == '留言区':
    page4()
elif page == '音乐':
    page5()
