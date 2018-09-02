age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')



age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
# s = input('birth: ')
s = 0
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

#遍历有序集合 list
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#遍历列表并计算list
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

#生成一个整数序列，list()函数可以转换为list
print(list(range(5)))


#while循环计算所有的值
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#break跳出while循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


#continue可以跳出本次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)