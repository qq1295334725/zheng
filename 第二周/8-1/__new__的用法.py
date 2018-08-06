"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:__new__的用法.PY
@ide:PyCharm
@time:2018-08-01 14:03:50
"""
# __new__方法主要是当你继承一些不可变的class时（比如int，str，tuple），提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。
class A(object):
    def __init__(self):
        print('这是__init__方法')

    def __new__(cls):
        print('这是__new__方法')
        return object.__new__(cls)

a = A()
# __new__至少有一个参数cls，代表要实例化的类，cls这个参数是在实例化时，由python自动提供的。
# __new__必须要有返回值，返回的实例化出来的实例。
# __init__有一个参数self，就是这个__new__返回的实例，__new__函数就可以在基础上完成一些初始化的操作。
# 我们可以把类当做制造商，__new__方法就是前期的原材料购买环节，__init__方法就可以在原材料的基础上进行加工，初始化商品。用于在生成对象之前可以加一步操作。


