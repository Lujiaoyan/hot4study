'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的手页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write()
    st.image()
    
def page_2():
    '''我的图片处理工具'''
    st.write()
    st.image()
    
def page_3():
    '''我的智慧词典'''
    st.write()
    st.image()

def page_4():
    '''我的留言区'''
    st.write()
    st.image()

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()