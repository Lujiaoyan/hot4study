'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的手页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    st.write('看我的兴趣推荐')
    st.image('ClassIn_20240804210232.jpeg')
    
def page_2():
    '''我的图片处理工具'''
    pass
    
def page_3():
    '''我的智慧词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
