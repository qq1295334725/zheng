"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:__str__的用法.PY
@ide:PyCharm
@time:2018-08-01 10:50:54
"""
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__:当使用print输出对象的时候，只要定义了__str__(self)这个办法，那么就会打印出这个方法中return出来的数据。
    def __str__(self):
        return '现在是%s这个对象'%self.name



s = Student('张三', '20')
print(s)
s1 = Student('李四', '21')
print(s1)

# 在python中如果一个方法名是__**__()的，那么这个函数就有特殊的功能，因此都称为魔法方法。













