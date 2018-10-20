#!/usr/bin/python
# -*- coding: UTF-8 -*- 
 
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配 (0, 3)
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配 None


line = "Cats are smarter than dogs"
 

# re.match(pattern, string, flags=0)
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")


# re.search 扫描整个字符串并返回第一个成功的匹配。re.search(pattern, string, flags=0)
zzz = re.search('www', 'www.runoob.com').span()  # 在起始位置匹配 (0, 3)
print(zzz[0],zzz[1])
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配 (11, 14)


a = 'www.runoob.com'
print(a[0])  # w
print(a[0:3]) # www


# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
# 函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
# re.sub(pattern, repl, string, count=0, flags=0) count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("替换结果 ", num) #返回替换结果，原字符串未被替换
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone) # \d匹配任意数字，\D是匹配任意非数字
print("替换结果 : ", num)

# 原字符串在sub之后其实并没有任何改变的
print(phone)  # 2004-959-559 # 这是一个国外电话号码