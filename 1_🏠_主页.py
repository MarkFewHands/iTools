# -*- coding: utf-8 -*-
# @Author  : MarkfewHands
# @Desc    : 

import streamlit as st 
import sys
from config import *
PublicPartInit(sys.argv[0].split('.')[0])


st.write('#### 码几手的工具箱', anchor = 'Home')
st.caption(about_me_text)

'---'
'#### 工具列表'
st.caption('手机端用户可在左上角 > 展开侧边栏选择对应的工具')

'''
+ [造假大师](/造假大师)  
+ [json格式化](/json格式化)

'''

'---'
'#### 用户交流'
'> [点击进入](https://support.qq.com/product/433845)'
