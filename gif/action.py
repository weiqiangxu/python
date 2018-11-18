#!/bin/python3
# -*- coding: UTF-8 -*-

# 导入模块
import create
import os,sys
import shutil


# 王境泽动态表情包生成
def wang(one_txt='',two_txt='',three_txt='',four_txt=''):
	# gif生成png
	tmp_dir = create.processImage('wangjingze.gif')
	# 开始加文字
	one_pics = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png','12.png','13.png','14.png','15.png','16.png','17.png']
	two_pics = ['18.png','19.png','20.png','21.png','22.png','23.png','24.png','25.png','26.png']
	three_pics = ['27.png','28.png','29.png','30.png','31.png','32.png','33.png','34.png','35.png','36.png','37.png','38.png','39.png']
	four_pics = ['40.png','41.png','42.png','43.png','44.png','45.png','46.png','47.png','48.png','49.png','50.png','51.png','52.png']
	for pic in one_pics:
		create.add_text(tmp_dir+'/'+pic,one_txt,x=50,y=133,font_size=16)
	print('one_txt')
	for pic in two_pics:
		create.add_text(tmp_dir+'/'+pic,two_txt,x=50,y=133,font_size=16)
	print('two_txt')
	for pic in three_pics:
		create.add_text(tmp_dir+'/'+pic,three_txt,x=50,y=133,font_size=16)
	print('three_txt')
	for pic in four_pics:
		create.add_text(tmp_dir+'/'+pic,four_txt,x=50,y=133,font_size=16)
	print('four_txt')
	# 图片拼成gif
	gif_name = create.create_gif(tmp_dir)
	# 删除整个目录
	shutil.rmtree(tmp_dir) 
	print(gif_name)


wang('我就是用华为','用诺基亚','也不会买你们苹果公司的产品','iphone7真好用')