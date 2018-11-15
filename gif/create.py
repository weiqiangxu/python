from PIL import Image
import sys
import matplotlib.pyplot as plt
import imageio,os

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


# 多张png图片生成gif
def create_gif(save_file):
    images = []
    filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
    for filename in filenames:
        images.append(imageio.imread(filename)) 
    imageio.mimsave(save_file, images,duration=1)

# create_gif('new.gif')