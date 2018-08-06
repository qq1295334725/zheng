"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:self对象.PY
@ide:PyCharm
@time:2018-07-30 14:04:18
"""
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('self=', self)
    def show(self):
        print('调用了show函数')
        # print('self=====', self)
# self其实本身指代的就是一个对象，这个对象是Student类类型的，self具体指代的是Student哪一个对象，是由Student中的哪一个对象在使用属性或者函数（方法）来决定的。
print(Student('张三', '20'))
stu = Student('张三', '20')
stu_1 = stu
print(stu)
print(stu_1)
# print(stu)
# print(stu.name)
# stu.show()

stu_one = Student('李四', '22')
print(stu_one)
stu_one = Student('王五', '22')
print(stu_one)
# stu_one.show()

# 面试常问：
# 对象的内存具有唯一性，两个不同的对象内存是不一样的。
# stu和Student('张三','20')之间的关系。
# 第一步：当 Student('张三'，'20')执行完的时候，实际上已经实例化出来了一个对象，与此同时对象在内存中已经产生。
# 第二步：将内存中已经产生的这个对象赋值给了stu这个变量（指针），使用这个变量（指针）来代替Student('张三','20')这个对象来执行函数的调用，属性的调用。
# 指针是用于指向一个对象的内存地址，方便去操作对象，管理对象。
# 一个对象内存地址可以由多个指针进行指向。但是一个指针只能指向一个对象的内存地址。



