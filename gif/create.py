#!/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image,ImageFont,ImageDraw
import sys
import matplotlib.pyplot as plt
import imageio,os
import re
import io
import time;  # 引入time模块

# Fix命令行中文输出乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


# gif图片生成多张png
def processImage(gif_dir):
    # 创建存储路径
    save_dir = time.strftime("%Y%m%d%H%M%S", time.localtime())
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        im = Image.open(gif_dir)
        i = 1
        mypalette = im.getpalette()
        try:
            while 1:
                im.putpalette(mypalette)
                new_im = Image.new("RGBA", im.size)
                new_im.paste(im)
                new_im.save(save_dir+'/'+str(i)+'.png')
                i += 1
                im.seek(im.tell() + 1)
        except EOFError:
            pass # end of sequence
    except Exception as e:
            # 捕获异常
            print(e)
    return  save_dir


# 将文件夹内部所有png转为gif
def create_gif(image_dir,speed_num = 0.3):
    gif_name = time.strftime("%Y%m%d%H%M%S"+'.gif', time.localtime())
    image_list=[]
    # 循环文件夹
    for img in os.listdir(image_dir):
        if(img.endswith('.png')):
            image_list.append(image_dir+'/'+img)
    # gif源文件列表
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = speed_num)  
    return gif_name


# 在图片上添加文字
def add_text(image_dir,content,x=0,y=0,font_size=14):
    try:
        #打开底版图片
        img=Image.open(image_dir)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('simsun.ttc',font_size)
        text = content
        draw.text((x, y),text,(255,255,255),font=font)
        draw = ImageDraw.Draw(img)
        img.save(image_dir)
    except Exception as e:
            # 捕获异常
            print(e)

# add_text('target.png','爱你洛溪',19,80)
# sdir = processImage('wangjingze.gif')