"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:单例类.PY
@ide:PyCharm
@time:2018-08-01 14:12:40
"""
# 单例类：就某一个类只能生成一个对象
class Singleton(object):
    __instance = None
    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance

a = Singleton()
a1 = Singleton()
a2 = Singleton()
print(a)
print(a1)
print(a2)


