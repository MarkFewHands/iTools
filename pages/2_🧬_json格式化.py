# -*- coding: utf-8 -*-
# @Author  : MarkfewHands
# @Desc    :

import streamlit as st
import sys
from config import *
PublicPartInit(sys.argv[0].split('.')[0])

st.info('工具介绍：对json对象进行格式化')
example_json = "{'物品': {'钢笔': {'颜色': '黑色', '数量': 100}},'地点': {'省': '广东','市':'广州'},'人物': {'性别': '男', '年龄': 18, '是否单身狗': False}}"
true = True; false = False; null = NUll = None

with st.form("format_str"):
    json_str = st.text_area(label = '粘贴需要格式化的json内容', value = example_json, height = 500, max_chars = 500000)
    if st.form_submit_button("格式化"):
        st.json(eval(json_str))