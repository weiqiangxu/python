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

# 发送get请求
keywd = 'hello'
url = 'http://www.baidu.com/s?wd='+keywd
# 构建一个request对象
req=urllib.request.Request(url)
# 打开对应的Request对象
data=urllib.request.urlopen(req).read()
fhandle=open('./1.html','wb')
fhandle.write(data)
fhandle.close()



#post请求
import urllib.request
import urllib.parse
url = 'http://www.baidu.com'
postdata = urllib.parse.urlencode({
	"name":"jack",
	"pass":'123456'
	}).encode('utf-8') #将数据使用urlencode处理后，使用encode设置为utf8编码
req.add_header('User-Agent','Mozilla')
data = urllib.request.urlopen(req).read()
fhandle=open('./1.html','wq')
fhandle.write(data)
fhandle.close()


# 使用代理服务器
def use_prox


