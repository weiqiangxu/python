#python很神奇的一个变量 - 字典 - 用于快速获取字段映射
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#删除字段的元素
#dict的key必须是不可变对象
d.pop('Bob')


# set数据格式 - 内部元素不能重复

s = set([1, 2, 3])
print(s)

 # # 通过add(key)方法可以添加元素到set中
s.add(4);

s.add(4);
 # # 因为内部元素不会重复，所以你无论添加几次，都不会有效果
s.remove(3)


print(s)


# 两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)


# str是不变对象，而list是可变对象。

a = 'abc'

print(a.replace('a', 'A'));


# 这点跟PHP很不一样，PHP的replace会改变a变量本身，而py不会
print(a)