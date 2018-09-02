#有序集合list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#获取有序集合的长度
print(len(classmates))

print(classmates[2])

#访问最后一个元素 - 也可以通过len函数获取元素长度
print(classmates[-1])

#追加元素到集合之中
classmates.append('Adam')
print(classmates)

#追加元素到集合指定的位置
classmates.insert(1, 'Jack')
print(classmates)

#删除集合尾部的元素 - 返回值是被删除的元素
print(classmates.pop())
print(classmates)

#删除指定元素-这个1是第二个元素的意思
classmates.pop(1)
print(classmates) 

#替换元素
classmates[1] = 'Sarah'
print(classmates)

#二维数组
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))


#无法改变的有序列表 - 元祖
t = ('a', 'b', ['A', 'B'])
print(t)
#虽然没有insert、append那些方法，但是仍然可以通过改变内部元素的值改变touble -（MMP）
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

#看到没，其实上面的也没有改变touble的指向，只是改变了touble里面的元素的指向 ，
#所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变 ，但里面的每个元素指向的这个list本身是可变的！