"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:454545.PY
@ide:PyCharm
@time:2018-07-26 21:47:06
"""
res = [ x*y for x in range(0,10) for y in range(0,10)]
print(res)
'''
类：用来描述具有相同的属性和方法的对象的集合,它定义了该集合中的每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数
类变量：类变量在整个实例化的对象中是公用的。类变量通常不作为实例变量使用。

'''

class ClassName:
    i = 1,2,3
    def f(self):
        return 'hello wrold'
# x = ClassName()
print('类的属性i为',ClassName.i)
print('类的方法f输出为：',ClassName.f(1))
# print(id(ClassName.f()))

# def __init__(self):
#     self.data = []
# x = ClassName

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, 4.3)
print(x.i, x.r)
print('')

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()

class People:
    name = ''
    __age = 0
    def __init__(self, n, a):
        self.name = n
        self.__age = a
        print(self.__age)
    def speak(self):
        print('%s12'%(self.name))
p = People('发电风扇',34)
p.speak()
print(p.name)
print(p.__init__('方大王',20))








