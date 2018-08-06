"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:121113333.PY
@ide:PyCharm
@time:2018-07-30 14:47:58
"""
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('show函数被执行')
print(Student('aa', '30'))
print('')
stu_1 = Student('aa', '30')
print(Student('aa', '30'))
print('')
stu = stu_1
print(stu)
print(stu_1)

print('')
stu_2 = Student('qq', '11')
print(stu_2)






















