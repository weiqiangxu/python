#!/usr/bin/python3

import threading
import time
import urllib.request

# 以下请求地址：
# <?php
# sleep(2);
# echo json_encode(array('status'=>true,'data'=>'hello world!'));

class myThread (threading.Thread):
    def __init__(self, url, file_name):
        threading.Thread.__init__(self)
        self.url = url
        self.file_name = file_name
    def run(self):
        file = urllib.request.urlopen(self.url)
        data = file.read()
        # 获取响应内容
        print(data)


# 创建新线程
thread1 = myThread('http://localhost/test.php?id=1','1.log')
thread2 = myThread('http://localhost/test.php?id=2','2.log')
thread3 = myThread('http://localhost/test.php?id=3','3.log')
thread4 = myThread('http://localhost/test.php?id=4','4.log')
thread5 = myThread('http://localhost/test.php?id=5','5.log')
thread6 = myThread('http://localhost/test.php?id=6','6.log')
thread7 = myThread('http://localhost/test.php?id=7','7.log')
thread8 = myThread('http://localhost/test.php?id=8','8.log')
thread9 = myThread('http://localhost/test.php?id=9','9.log')
thread10 = myThread('http://localhost/test.php?id=10','10.log')

# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()

# 等待至线程中止
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
thread10.join()