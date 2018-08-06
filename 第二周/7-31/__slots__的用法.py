"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:__slots__的用法.PY
@ide:PyCharm
@time:2018-07-31 09:18:04
"""
# __slots__:主要用于限制一个类的对象能添加的属性有哪些
class People(object):
    # 以元组的形式，定义要添加的属性，除此之外的属性不能被添加，即对动态绑定的属性发挥作用，也对__init__函数当中添加的属性发挥作用。
    __slots__ = ('name', 'age', 'weight')
    def __init__(self, name, age,weight):1
        self.__name = name
        self.age = age
        self.weight = weight
        # self.height = height

p1 = People('张三','20','180')
# print(p1.height)
# p1.height='172'
# print(p1.height)

