'''我的作品'''
import streamlit as st
page = st.sidebar.radio("我的首页",['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page1():
    '''我的兴趣推荐'''
    st.write('欢迎来到我的兴趣推荐~')
    st.image("h3R3.jpg")
    
def page2():
    '''我的图片处理工具'''
    pass
def page3():
    '''我的智慧词典'''
    pass
def page4():
    '''我的留言区'''
    pass

if page == "我的兴趣推荐":
    page1()
elif page == "我的图片处理工具":
    page2()
elif page == "我的智慧词典":
    page3()
elif page == "我的留言区":
    page4()
