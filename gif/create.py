#!/bin/python3

from PIL import Image
import sys
import matplotlib.pyplot as plt
import imageio,os
import re
# gif图片生成多张png
def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print ("Cant load", infile)
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()
    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save('a'+str(i)+'.png')
            i += 1
            im.seek(im.tell() + 1)
    except EOFError:
        pass # end of sequence

# processImage('wangjingze.gif')


# 将文件夹内部所有png转为gif
def create_gif(image_dir, gif_name):
    image_list=[]
    # 循环文件夹
    for img in os.listdir(image_dir):
        if(img.endswith('.png')):
            image_list.append(image_dir+'/'+img)
    print(image_list)
    # gif源文件列表
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)  
    return


create_gif('./image','new.gif' )