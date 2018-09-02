# 下面我们开始学习高级特性

# 情景：我们需要构造一个1, 3, 5, 7, ..., 99的列表

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

# 但是还是代码太长了，学习了高级特性，我们可以一行代码搞定哦，下面开始

# 切片

# 取前面三种元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
     r.append(L[i])
print(r)

# 最简单的方式 - 0至3但是不包括3哦 也就是索引伟 0 1 2 
L[0:3]
# 倒数切片
print(L[-2:])
print(L[-2:-1])

# L[开始位:结束位:间隔]
# demo 创建一个0-99的数列
L = list(range(100))
# print(L)
# 比如前10个数：
# 后10个数：
# 前11-20个数：
# 前10个数，每两个取一个：
# 所有数，每5个取一个：

# tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串也可以用切片操作，只是操作结果仍是字符串

print('ABCDEFG'[:3])

# 迭代： java的迭代如下
# for (i=0; i<list.length; i++) {
#     n = list[i];
# }

# python的迭代就不一样了，更加抽象：
# dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)

# 字符串也是可迭代对象
for ch in 'ABC':
	print(ch)

# 通过collections模块的Iterable类型判断是否是可迭代对象
# from collections import Iterable
# isinstance('abc', Iterable) # str是否可迭代 true
# isinstance([1,2,3], Iterable) # list是否可迭代 true
# isinstance(123, Iterable) # 整数是否可迭代 - false

# 字典迭代获取key下标我们知道，但是list的下标呢 ，通过enumerate函数把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)


# 列表生成式
list(range(1, 11))

L = []
for x in range(1, 11):
	L.append(x*x)


# 可以一行搞定哦：
Z = [x * x for x in range(1,11)]

# 可以给选择x的时候添加条件

O = [x * x for x in range(1,11) if x%2 == 0]
print(O)

# 两层循环
P = [m + n for m in 'ABC' for n in 'XYZ']
print(P)

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现： 真的很强
import os # 导入os模块，模块的概念后面讲到 - 
T =  [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(T)

# 列表生成式转小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])