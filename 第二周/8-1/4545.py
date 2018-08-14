"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:4545.PY
@ide:PyCharm
@time:2018-08-01 19:28:12
"""
# class Dog(object):
#     __slots__ = ('name', 'age', 'work1')
#     def __init__(self, name, age, work1):
#         self.name = name
#         self.age = age
#         self.work1 = work1
#     def name1(self):
#         print('你好')
#     @classmethod
#     def work(cls):
#         print('父类')
# class DDog(Dog):
#     def __init__(self, name,work1, page):
#         super(DDog,self).__init__(self,name,work1)
#         self.name = name
#         self.work1 = work1
#         self.page = page
#     def name2(self):
#         print('子类name2')
#     def work(cls):
#         print('子类')
# d1 = Dog('二狗子','8','吃')
# d1.work()
# Dog.work()
# d1.name1()
# Dog.name1(1)
class People(object):
    def __init__(self,name,age,height):
        self.name = name
        self.__height = height
        self.__age = age
    @property
    def work(self):
        return self.__height,self.__age

    @work.setter
    def work(self,height):
        if isinstance(height,int):
            self.__height = height
        else:
            raise ValueError('错误111')

    @work.deleter
    def work(self):
        if hasattr(self,'_People__age'):
            del self.__age
            print('1111111111')
        else:
            print('www')
            # raise ValueError('www')
s1 = People('张三', 20, 180)
r1 = s1.work
print(r1)
s1.work=188
print(s1.work)
del s1.work


































