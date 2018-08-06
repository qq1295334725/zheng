"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:类的声明.PY
@ide:PyCharm
@time:2018-07-30 10:51:45
"""
class People(object):
    # __init__：这个初始化函数，会在对象被创建的时候，自动执行函数的调用，不需要手动的打点调用。
    # __init__():在类中并不是必须定义的，但是当声明属性的时候，必须通过__init__函数声明。
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print('我是在对象被创建出来的时候自动被调用执行的')
    # 类中定义的函数，第一个参数必须是self，self也相当于一个形参，但是它是由解释器自动传真。self后面可以定义我们需要的参数。
    def sleep(self):
        print('睡觉')

    def eat(self):
        print('吃饭')

    def work(self):
        print('工作')

# 当创建p1这个对象的时候，自动执行了对象的初始化函数__init__(),并且给初始化函数传递了参数。传递参数的时候，参数中实际上隐含了一个实参，这个实参会赋值给__init__函数中的self形参。
p1 = People('p1', '20', '男')
# 当对象操作类中的属性的时候，对象名.属性名，操作类中函数的时候，对象名.函数名（）
print(p1.name)
p1.work()
# 关于对象的创建过程（对象内存）：
# 每一次通过People类创建对象的时候，python解释器都会给对象分配一个单独的内存空间，会将People类中定义的属性复制一份存放到对象的内存中，同时，内存具有唯一性的特征，创建出来的每一个对象都是惟一的，独立的，不允许重复。
# 虽然所有People类的对象都是复制了name，age，sex这些属性，但是复制出来的每一个属性都是存在各自内存中的，每个对象的属性互不相干。
p2 = People('p2', '30', '女')
print(id(p1))
print(id(p2))


