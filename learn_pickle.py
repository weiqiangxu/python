#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 序列化对象持久化存储pickle

# pickle.dump(obj, file, [,protocol])
# pickle.load(file)

import pickle

a = {" name ": "Tom", "age": "40"} #字典

# 存储
with open('text.txt', 'wb') as file:
	pickle.dump(a, file)

# 打开
with open('text.txt', 'rb') as file2:
	b = pickle.load(file2)

print(type(b))

print(b)