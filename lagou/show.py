#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取pkl文件

import pickle as pk
f = open('info.pkl','rb')
info = pk.load(f)  
print(info)   #show file  