"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:父类方法的重写.PY
@ide:PyCharm
@time:2018-08-01 09:13:15
"""
# 子类重写父类方法
# 1.完全重写，子类不继承父类所有函数的功能，直接将父类的函数的功能进行覆盖
# 2.部分重写，父类函数中的功能符合子类的需求，但是还需要添加一些功能。


# 注意点
# 1.子类重写父类的方法中，子类中定义的函数名必须和父类的函数名保持一致.
# 2.使用super(子类名，self)函数是部分重写,不使用super()函数是完全重写.

class People(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def work(self):
        print('我是父类当中的work函数')

class Man(People):
    def __init__(self, name, age, height, sex, weight):
        # super函数，是让Man类对象self，调用父类的初始化函数__init__()。
        super(Man, self).__init__(name, age, height)
        self.name = name
        self.age = age
        self.height = height
        self.sex = sex
        self.weight = weight
        print('子类的初始化函数')
    def work(self):
        print('我重写了父类的work函数')
        print('好开森')
        print('我是子类的work函数')


p1 = People('张三', '20', '180')
m1 = Man('李四', '22', '190', '男', '180')
print(m1.name)
print(m1.sex)
m1.work()


# 例子
class Student(object):
    file_test = open('student.txt', 'w', encoding='utf-8')
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def save_data(self):
        Student.file_test.write(self.name+' '+self.score)

    def close_file(self):
        Student.file_test.close()

# s1 = Student('张三', '180')
# s1.save_data()
# s1.close_file()

class ReadStudent( Student):
    # 部分重写父类的save_data方法
    def save_data(self):
        super(ReadStudent, self).save_data()
        ReadStudent.file_test.close()
        # 添加读取的功能
        f = open('student.txt', 'r', encoding='utf-8')
        res = f.readline()
        print('读取的结果是：',res)

s2 = ReadStudent('李四', '98')
s2.save_data()


