import streamlit as st

page = st.sidebar.radio('我的主页',['我的兴趣推荐', '我的图片处理', '我的智慧词条', '我的留言区'])
def page1():
    '''兴趣推荐'''
    pass
def page2():
    '''图片处理'''
    st.image('2.png')
def page3():
    '''智慧词条'''
    pass
def page4():
    st.write(['hi'])
    pass

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理':
    page2()
elif page == '我的智慧词条':
    page3()
elif page == '我的留言区':
    page4()
