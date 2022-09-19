# -*- coding: utf-8 -*-
# @Author  : MarkfewHands
# @Desc    :

import streamlit as st

forum_url = 'https://support.qq.com/product/433845'
post_url = 'https://support.qq.com/embed/phone/433845/new-post'

about_me_text = '''
一名业余程序员，工作中喜欢把繁琐的流程化的工作用代码(Python)来实现，利用自动化办公代码解放双手。  
在互联网时代，始终觉得自己也是个手艺人，传统手艺人做的是现实世界的实物，我做的是针对“计算机”而言的工具。  
在这里主要记录和分享自己觉得一些有用的在线工具，希望可以帮助到大家。  
当然，如果大家觉得有一些想实现的在线工具，或者使用过程遇到什么问题，都可以通过[这里](https://support.qq.com/embed/phone/433845/new-post)反馈，我尽我所能更新给大家❤️❤️  
Python学习交流可以关注公众号【码几手】❤️
'''


classifier = {
    '人物': {
        '姓名': 'fake.name()',
        '姓名(男)': 'fake.name_male()',
        '姓名(女)': 'fake.name_female()',
        '姓': 'fake.last_name()',
        '名字': 'fake.first_name()',
        '名字(男)': 'fake.first_name_male()',
        '名字(女)': 'fake.first_name_female()',
    },
    '地址': {
        '地址': 'fake.address()',
        '楼名': 'fake.building_number()',
        '完整城市名': 'fake.city()',
        '城市名字(不带市县)': 'fake.city_name()',
        '城市后缀名': 'fake.city_suffix()',
        '国家名称': 'fake.country()',
        '地区': 'fake.district()',
        '邮编': 'fake.postcode()',
        '省': 'fake.province()',
        '街道地址': 'fake.street_address()',
        '街道名称': 'fake.street_name()',
        '街道后缀名': 'fake.street_suffix()',
        '国家编号': 'fake.country_code(representation="alpha-2")',
    },
    '条形码': {
        'EAN条形码': 'fake.ean(length=13)',
        'EAN13条形码': 'fake.ean13()',
        'EAN8条形码': 'fake.ean8()'
    },
    '汽车': {
        '牌照': 'fake.license_plate()'
    },
    '银行': {
        '银行所属国家': 'fake.bank_country()',
        '基本银行账号': 'fake.bban()',
        '国际银行代码': 'fake.iban()'
    },
    '颜色': {
        '颜色名称': 'fake.color_name()',
        '颜色十六进制值': 'fake.hex_color()',
        '颜色RGB值': 'fake.rgb_color()',
        'CSS颜色值': 'fake.rgb_css_color()',
        '安全色': 'fake.safe_color_name()',
        '安全色十六进制值': 'fake.safe_hex_color()'
    },
    '公司': {
        '商业用词': 'fake.bs()',
        '妙句(口号)': 'fake.catch_phrase()',
        '公司名称': 'fake.company()',
        '公司名称前缀': 'fake.company_prefix()',
        '公司名称后缀': 'fake.company_suffix()',
        '职位': 'fake.job()'
    },
    '信用卡': {
        '过期年月': 'fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")',
        '完整信用卡信息': 'fake.credit_card_full(card_type=None)',
        '信用卡卡号': 'fake.credit_card_number(card_type=None)',
        '信用卡提供商': 'fake.credit_card_provider(card_type=None)',
        '信用卡安全码': 'fake.credit_card_security_code(card_type=None)'},
    '货币': {
        '加密货币代码+名称': 'fake.cryptocurrency()',
        '加密货币代码': 'fake.cryptocurrency_code()',
        '加密货币名称': 'fake.cryptocurrency_name()',
        '货币代码+名称': 'fake.currency()',
        '货币代码': 'fake.currency_code()',
        '货币名称': 'fake.currency_name()'
    },
    '时间': {
        'AM或PM':
        'fake.am_pm()',
        '世纪': 'fake.century()',
        '日期字符串(可设置格式和最大日期)': 'fake.date(pattern="%Y-%m-%d", end_datetime=None)',
        '日期(可设置限定范围)': 'fake.date_between(start_date="-30y", end_date="today")',
        '日期(可设置最大日期)': 'fake.date_object(end_datetime=None)',
        '出生日期': 'fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)',
        '本世纪日期': 'fake.date_this_century(before_today=True, after_today=False)',
        '本年代中的日期': 'fake.date_this_decade(before_today=True, after_today=False)',
        '本月中的日期': 'fake.date_this_month(before_today=True, after_today=False)',
        '本年中的日期': 'fake.date_this_year(before_today=True, after_today=False)',
        '日期和时间': 'fake.date_time(tzinfo=None, end_datetime=None)',
        '日期和时间(从001年1月1日到现在)': 'fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)',
        '日期时间(可设置限定范围)': 'fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)',
        '本世纪中的日期和时间': 'fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)',
        '本年代中的日期和时间': 'fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)',
        '本月中的日期和时间': 'fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)',
        '本年中的日期和时间': 'fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)',
        '几号': 'fake.day_of_month()',
        '星期几': 'fake.day_of_week()',
        '未来日期': 'fake.future_date(end_date="+30d", tzinfo=None)',
        '未来日期和时间': 'fake.future_datetime(end_date="+30d", tzinfo=None)',
        'iso8601格式日期和时间': 'fake.iso8601(tzinfo=None, end_datetime=None)',
        '第几月': 'fake.month()', '月份名称': 'fake.month_name()',
        '过去日期': 'fake.past_date(start_date="-30d", tzinfo=None)',
        '过去日期和时间': 'fake.past_datetime(start_date="-30d", tzinfo=None)',
        '时间(可设置格式和最大日期时间)': 'fake.time(pattern="%H:%M:%S", end_datetime=None)',
        '时间间隔': 'fake.time_delta(end_datetime=None)',
        '时间(可设置最大日期时间)': 'fake.time_object(end_datetime=None)',
        '时区': 'fake.timezone()',
        'UNIX时间戳': 'fake.unix_time(end_datetime=None, start_datetime=None)',
        '某年': 'fake.year()'
    },
    '文件': {
        '文件扩展名': 'fake.file_extension(category=None)',
        '文件名': 'fake.file_name(category=None, extension=None)',
        '文件路径': 'fake.file_path(depth=1, category=None, extension=None)',
        'MIME类型': 'fake.mime_type(category=None)',
        'UNIX设备': 'fake.unix_device(prefix=None)',
        'UNIX分区': 'fake.unix_partition(prefix=None)'
    },
    '坐标': {
        '坐标': 'fake.coordinate(center=None, radius=0.001)',
        '纬度': 'fake.latitude()',
        '经纬度': 'fake.latlng()',
        '返回某个国家某地的经纬度': 'fake.local_latlng(country_code="US", coords_only=False)',
        '返回地球上某个位置的经纬度': 'fake.location_on_land(coords_only=False)',
        '经度': 'fake.longitude()'
    },
    '网络': {
        '企业邮箱(ascii编码)': 'fake.ascii_company_email()',
        '企业邮箱+免费邮箱(ascii编码)': 'fake.ascii_email()',
        '免费邮箱(ascii编码)': 'fake.ascii_free_email()',
        '安全邮箱(ascii编码)': 'fake.ascii_safe_email()',
        '企业邮箱': 'fake.company_email()',
        '域名': 'fake.domain_name(levels=1)',
        '二级域名': 'fake.domain_word()',
        '企业邮箱+免费邮箱': 'fake.email()',
        '免费邮箱': 'fake.free_email()',
        '免费邮箱域名': 'fake.free_email_domain()',
        '主机名': 'fake.hostname()',
        '图片URL': 'fake.image_url(width=None, height=None)',
        'ipv4': 'fake.ipv4(network=False, address_class=None, private=None)',
        'ipv4网络等级': 'fake.ipv4_network_class()',
        '私有ipv4': 'fake.ipv4_private(network=False, address_class=None)',
        '公共ipv4': 'fake.ipv4_public(network=False, address_class=None)',
        'ipv6': 'fake.ipv6(network=False)',
        'MAC地址': 'fake.mac_address()',
        '安全邮箱': 'fake.safe_email()',
        'URL中的slug': 'fake.slug()',
        '顶级域名': 'fake.tld()', 'URI': 'fake.uri()',
        'URI扩展': 'fake.uri_extension()',
        'URI页': 'fake.uri_page()',
        'URI路径': 'fake.uri_path(deep=None)',
        'URL': 'fake.url(schemes=None)',
        '用户名': 'fake.user_name()'
    },
    '图书': {
        'ISBN-10图书编号': 'fake.isbn10(separator="-")',
        'ISBN-13图书编号': 'fake.isbn13(separator="-")'
    },
    '文本': {'单个段落': 'fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)',
           '多个段落': 'fake.paragraphs(nb=3, ext_word_list=None)',
           '单个句子': 'fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)',
           '多个句子': 'fake.sentences(nb=3, ext_word_list=None)',
           '单个文本': 'fake.text(max_nb_chars=200, ext_word_list=None)',
           '多个文本': 'fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)',
           '单个词语': 'fake.word(ext_word_list=None)',
           '多个词语': 'fake.words(nb=3, ext_word_list=None, unique=False)'
           },
    '电话': {
        '完整手机号码(加了国家和国内区号)': 'fake.msisdn()',
        '手机号': 'fake.phone_number()',
        '区号': 'fake.phonenumber_prefix()'
    },
    '个人档案': {
        '档案(完整)': 'fake.profile(fields=None, sex=None)',
        '档案(简单)': 'fake.simple_profile(sex=None)'},
    '身份证': {
        '身份证号': 'fake.ssn(min_age=18, max_age=90)'
    },
    '用户设备/代理/浏览器等属性': {
        '安卓': 'fake.android_platform_token()',
        'Chrome UA': 'fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)',
        'FireFox UA': 'fake.firefox()',
        'IE UA': 'fake.internet_explorer()',
        'ios': 'fake.ios_platform_token()',
        'Linux': 'fake.linux_platform_token()',
        'Linux处理器': 'fake.linux_processor()',
        'Mac': 'fake.mac_platform_token()',
        'Mac处理器': 'fake.mac_processor()',
        'Opera UA': 'fake.opera()',
        'Safari UA': 'fake.safari()',
        '随机用户代理': 'fake.user_agent()',
        'Windows': 'fake.windows_platform_token()'
    }
}

pageConfig = {
    '1_🏠_主页': {
        'page_title': '我的工具箱',
        'page_icon': "https://img0.baidu.com/it/u=2473071638,2532945697&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",
        'layout': 'wide',
        'About': '# 在线小工具'
    },
    '1_📈_造假大师': {
        'page_title': '造假大师',
        'page_icon': "https://img1.baidu.com/it/u=2318852377,3517315434&fm=253&fmt=auto&app=138&f=JPEG?w=260&h=261",
        'layout': 'wide',
        'About': '#### 批量生成测试/假数据，就是这么简单~'
    },
    '100_⛽️_更多': {
        'page_title': '持续更新',
        'page_icon': 'https://img1.baidu.com/it/u=2318852377,3517315434&fm=253&fmt=auto&app=138&f=JPEG?w=260&h=261',
        'layout': 'wide',
        'About': '# 关注公众号，获取更新'
    },
    
}

def PublicPartInit(file_name):
    st.set_page_config(
        page_title = pageConfig[file_name]['page_title'],
        page_icon = pageConfig[file_name]['page_icon'],
        layout = pageConfig[file_name]['layout'],
        menu_items={
            'Get Help': post_url,
            'Report a bug': post_url,
            'About': pageConfig[file_name]['About']
        }
    )
    st.sidebar.image('./data/qrcode.jpg',caption = '欢迎关注我的公众号', width = 150)
    st.sidebar.write('> [反馈&留言](https://support.qq.com/embed/phone/433845/new-post)')