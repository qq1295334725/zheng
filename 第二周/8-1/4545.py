"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:4545.PY
@ide:PyCharm
@time:2018-08-01 19:28:12
"""
# class Student(object):
#     def __init__(self):
#         print('__init__')
#
#     def __new__(cls):
#         print('__new__')
#         return object.__new__(cls)
# Student()

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return '它是%s。'%self.name
#
# print(Student('sahg'))
# print(s1)

#
# class Student(object):
#     __instance = None
#     def __new__(cls):
#         if cls.__instance:
#             return cls.__instance
#         else:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
# a1 = Student()
# print(a1)
# a2 = Student()
# print(a2)

# class People(object):
#     def work(self):
#         pass
# class APeople(People):
#     def work(self):
#         print('吃')
# class BPeople(People):
#     def work(self):
#         print('完玩')
# class CPeople(People):
#     def work(self):
#         print('洗')
# def work_1(obj):
#     obj.work()
# p1 = APeople()
# # work_1(p1)
# p1.work()
# BPeople().work()

class Student(object):
    f = open('student.txt', 'w', encoding='utf-8')
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def write_file(self):
        Student.f.write(self.name+' '+self.score)
    def close_file(self):
        Student.f.close()
class StudentOne(Student):
    def read_file(self):
        super(StudentOne, self).write_file()
        StudentOne.f.close()
        f1 = open('student.txt', 'r', encoding='utf-8')
        res = f1.readline()
        return res

S1 = StudentOne('张三', '45')
print(S1.read_file())






















