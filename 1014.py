#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 下载优美图库首页所有图片 http://www.umei.cc/
# 使用xpath https://www.cnblogs.com/lei0213/p/7506130.html
# 使用beautiful soup http://www.runoob.com/w3cnote/python-spider-intro.html
import urllib.request
import re
import bs4
import sys

from bs4 import BeautifulSoup

# 下载html页面
def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html_doc = get_html('http://www.umei.cc/')


#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")

#获取所有的图片地址链接
links = soup.find_all('img')
for link in links:
	urllib.request.urlretrieve(link['src'], 'tieba.jpg')
    # print(link.name,link['src'])

# 终止程序
sys.exit()
