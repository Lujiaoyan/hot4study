"------我的主页------"
import streamlit as st

page=st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区"])

def page1():
    "我的兴趣推荐"
    st.write("这是我的兴趣推荐")
    st.image("ClassIn_20240804205303.jpg")

def page2():
    "我的图片处理工具"
    st.write("这是我的图片处理工具")
    st.image("5ee9db0cf2ef8efe5e4b25abcea520dc.jpeg")
    pass

def page3():
    "我的智慧词典"
    st.write("这是我的智慧词典")
    st.image("a0876a06baa8377fc22b307d71f9423c.jpeg")
    pass
    
def page4():
    "我的留言区"
    st.write("这是我的留言区")
    st.image("ClassIn_20240804205303.jpg")
    pass

if page=="我的兴趣推荐":
    page1()
elif page=="我的图片处理工具":
    page2()
elif page=="我的智慧词典":
    page3()
elif page=="我的留言区":
    page4()
    
