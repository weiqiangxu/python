#告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#!/usr/bin/env python3

#告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# -*- coding: utf-8 -*-

#数据类型和变量
print('I\'m ok.')

print('''line1
line2
line3'''
)

if 1==2:
    print('1==2')
else:
    print('1!=2')


a=123
print(a)


#相除一定取整数的
print(9//3)

#对于单字符可以转换为数字表示、以及将数字转换为字母
z = ord('A')
print(z)

c = chr(65)
print(c)

#计算字符长度
a = len('ABC')
print(a)

#字符编码转换
l = 'ABC'.encode('ascii')
print(l)
print(l.decode('ascii'))

c = '中文'.encode('utf-8')
print(c)
print(c.decode('utf-8'))

#len获取字符数|字节数
print(len('中文'))
print(len('中文'.encode('utf-8')))


#格式化
#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print( 'Age: %s. Gender: %s' % (25, True))

#第二种字符串格式化
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))