# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os, sys
import urllib.request
import threading
import time


# 下载图片对象
class myThread (threading.Thread):
    def __init__(self, url, file_name,dir_name):
        threading.Thread.__init__(self)
        self.url = url
        self.file_name = file_name
        self.dir_name = dir_name
    def run(self):
    	save_img(self.url,self.file_name,self.dir_name)
    	print('success')


# 保存图片
def save_img(img_url,file_name,file_path='img'):
	# 创建存储路径
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    #图片后缀
    file_suffix = os.path.splitext(img_url)[1]
    #拼接图片路径
    filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
    try:
        response = urllib.request.urlopen(img_url)
        pic = response.read()
        with open(filename,'wb') as f:
            f.write(pic)
    except Exception as e:
    	# 纯粹为了抑制错误
    	# file error ： HTTP Error 503: Service Temporarily Unavailable
        print('not acess')

# 抓取一个图集
def download_one(url,dir_name):
	if os.path.exists(dir_name)==False:
		os.mkdir(dir_name);
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	# 获取所有图片地址
	img_list = soup.find(id='tiles').find_all('img')
	img_urls = []
	for img in img_list:
		img = 'http://www.zhuamei5.com/'+img.get('src')  # 封面
		img = img.replace(".jpg.thumb", "")
		img_urls.append(img)
	# 创建线程对象
	threads = []
	i = 1
	for img in img_urls:
		thread = myThread(img,i,dir_name)
		threads.append(thread)
		i = i+1
	# 运行线程
	i = 1
	for thread in threads:
		print('thread start '+str(i))
		thread.start()
		i = i+1
	# 等待所有线程结束
	for thread in threads:
		thread.join()


		

# 下载xiao萌妹
download_one('http://www.zhuamei5.com/home.php?mod=space&uid=11279&do=album&id=944','kitty')


