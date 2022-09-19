# -*- coding: utf-8 -*-
# @Author  : MarkfewHands
# @Desc    :

import pandas as pd
import streamlit as st
from faker import Faker
import sys
sys.path.append('../')
from config import classifier, PublicPartInit
PublicPartInit(sys.argv[0].split('.')[0])

# @st.experimental_memo
def init_classifier_type(classifier=classifier):
    classifier_types = []
    for main_category in classifier:
        for sub_category in classifier[main_category]:
            classifier_types.append(f'{main_category}-{sub_category}')
    return classifier_types


if __name__ == '__main__':
    fake = Faker(locale='zh_CN')
    fake.name()
    cols_limit = 5
    rows_limit = 1500
    
    st.info('工具介绍：根据需求，选择对应数据类型生成虚拟数据，如姓名、电话、地址等信息。')
    col1, col2 = st.columns(2)
    with col1:
        choose_options = st.multiselect(
            f'请选择需要生成的数据类型(最多选择{cols_limit}类)', init_classifier_type(), default = ['公司-公司名称', '地址-地址'])
    with col2:
        rows = st.number_input(f'生成多少条假数据？(最多支持{rows_limit}行)', value=10, step=1)

    if rows > 1500 or len(choose_options) > 10:
        st.warning(f'暂仅支持生成最多{rows_limit}行，{cols_limit}列随机数据')
    else:
        data_dict = {}
        for item in choose_options:
            fun = classifier[item.split('-')[0]][item.split('-')[1]]

            data_dict[item] = ['/'.join(map(str, eval(fun))) if isinstance(eval(fun), list) else str(eval(fun)).replace('\n', '/') for i in range(int(rows))]
        data = pd.DataFrame(data_dict)
        st.markdown(data.to_markdown())
        
        st.write('\n')
        with st.expander('查看分类配置json'):
            st.info('以上数据通过python Faker模块自动生成，所有数据分类和实例化API请展开查看')
            st.json(classifier)
