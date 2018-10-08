#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
file = urllib.request.urlopen('http://www.xxsy.net/')
# 获取响应码
print(file.getcode())
# 获取请求的地址
print(file.geturl())
# 获取相应内容
data = file.read()

# urlencode
enco = urllib.request.quote('http://www.xxsy.net/')
# print(enco)

# urldecode
dec = urllib.request.unquote('http%3A//www.baidu.com')
# print(dec)


# 设置header请求
url = 'http://www.baidu.com'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

# 设置header请求的第二种方式
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
data=urllib.request.urlopen(req).read()


# 超时请求

for i in range(1,10):
	try:
		file=urllib.request.urlopen('http://www.baidu111.com',timeout=1)
		data=file.read()
		# 获取响应体的结构
		print(len(data))
	except Exception as e:
		print('catch except -->'+str(e))



# 将下载的内容存储
fhandle = open('./1.html','wb')
fhandle.write(data)
fhandle.close()

