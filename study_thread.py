#!/usr/bin/python3

import _thread
import time
import urllib.request
import pickle

# 为线程定义一个函数
def print_time( url, file_name):
  file = urllib.request.urlopen(url)
  # 获取响应内容
  print(file.getcode())
  data = file.read()
  # 存储
  fp = open(file_name,'w')
  fp.write(str(data))
  fp.close()

# 创建10个线程
try:
  _thread.start_new_thread(print_time,('http://localhost/test.php','1.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','2.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','3.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','4.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','5.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','6.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','7.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','8.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','9.log'))
  _thread.start_new_thread(print_time,('http://localhost/test.php','10.log'))
except:
  print ("Error: 无法启动线程")

# 等待子线程执行完成
time.sleep(3)
print('over')