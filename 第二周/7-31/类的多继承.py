"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:类的多继承.PY
@ide:PyCharm
@time:2018-07-31 16:10:44
"""
# 定义类A
class A(object):
    def print_test(self):
        print('A类')

class B(object):
    def print_test(self):
        print('B类')

class C(A, B):
    def print_test(self):
        print('C类')

# 面试题：
# 在上面的多继承的例子中，如果父类A还有父类B还有子类本身中都有一个同名的方法，那么通过子类调用的时候，会调用哪一个？
obj_c = C()
obj_c.print_test()
# 可以查看C类的对象搜索方法时的先后顺序。
print(C.__mro__)

















