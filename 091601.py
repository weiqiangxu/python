# 类和面向对象

# 定义一个类
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


bart = Student('Bart Simpson', 59)
print(bart.name)



# 定义一个方法
def print_score(std):
	print('%s: %s' % (std.name, std.score))


# 类内部的function如果加上双下划线__表示不会被外部访问