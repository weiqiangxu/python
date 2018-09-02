# 函数式编程
# 通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，
# 这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数



# qishi以上的几句话概括下来就是：python之中的函数可以是变量


f = abs
print(f(-10))

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# 以上就是一个简单的函数作为变量传递的demo

# map()函数接收两个参数，一个是函数

def f(x):
	return x*x

# 高阶函数map
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 返回结果
# 结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

print(list(r))


# gaojie函数reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x, y):
	return x+y


i = reduce(add, [1, 3, 5, 7, 9])
print(i)