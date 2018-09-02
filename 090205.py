# 一些简单的函数
print(abs(-3))

print(max(2, 3, 1, -5))

# 数据类型转换
print(int('123'))

float('12.34')

print(bool(1))

# 自定义函数

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x

# 引用文件内函数
from abstest import my_abs
print(my_abs(-99))

# 应用math包做一些简单的数学计算
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

# 返回两个值是一个假象，一般返回的变量是一个tuple
print(x,y)


# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程
# ax2 + bx + c = 0

def test(a,b,c,x):
	return a*x*x + b*x + c

print('hello ',test(1,2,3,1))

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

# 默认参数
def enrolls(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# python的默认函数的坑 - 由于没有函数内部变量作用域的概念 - 尼玛函数内部变量的L是全局的，而不是仅限于内部使用
def add_end(L=[]):
    L.append('END')
    return L

print(add_end()); ['END']

print(add_end()); ['END','END']

# 解决办法：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 问题探讨 写一个函数，可以计算 a*a + b*b + ...
# 可变参数

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(' 不可变参数函数这样调用: ',calc([1, 2, 3]))


# 可变参数
def calcc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 现在我们可以随意传参调用
print('可变参数这样调用',calcc(1, 2))
print('甚至可以完全不传参数',calcc())

nums = [1, 2, 3]
calcc(nums[0], nums[1], nums[2])
# 但是有时候，我们需要用touble或者list变量去完成，但是又不想想上面那个传递，我们可以：
calcc(*nums)




# 关键字参数 - 加入**  - 没加的那叫必选参数，加了的其实就是扩展字段
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
# 除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])


# 现在学习下递归参数 - 自身调用自身
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(6))

# 但是递归也有一个问题就是：
# 递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：