"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:类和对象.PY
@ide:PyCharm
@time:2018-07-30 09:54:22
"""
# 类和对象的基本定义:
# 类:具有相同属性或行为的事物统称为类.
# 对象:从类中具体实例化出来的一个具体事物的存在.

# 类和对象的关系:对象是类的实例,类是对象的模板.
# 区分类和对象:
# 1.车(类),王震宇的二手奥拓(对象)
# 2.狗(类),曹向阳的藏獒(对象)
# 3.水果(类),于胜阳啃的那个榴莲(对象)


# 面向对象编程中的类和对象:类在面向对象过程中,是一种抽象化的概念,类是不会占据内存空间的,类主要是为了辅助创建对象而存在的,对象才是面向对象编程的核心,所有函数的执行还有变量的调用都必须通过对象才能完成,对象在内存中是实际存在的,会消耗内存空间,对象也称为实例化对象.

# 面向对象过程中类的作用:通常情况下,会在类中指定一些属性和行为,当使用类实例化对象的时候,那么该对象就用于类中指定的属性和行为.

# 类是由每一个对象共同抽象化出来的概念,至于类中需要指定那些属性和行为,是由对象决定的,因为具体操作这些属性和行为的就是对象.

# 面向对象编程的时候,首先是考虑如何设计一个类,类中的属性和行为是对象需要的属性和行为共同决定的.

# 假如声明一个人类:
# 人类需要的属性:姓名,年龄,性别(属性:变量)
# 人类需要的行为:吃饭,睡觉,工作(行为:函数)

# class声明类的关键字
# People：自定义的一个类名，遵循大驼峰命名法
# object：表示当前类People的父类，也称为基类或者根类，表示的一种继承关系
class People(object):
    # __init__():对象的初始化函数，该函数就是用于指定对象属性的。
    # name/age/sex:叫做__init__函数的形参，等待着实参来传值
    def __init__(self, name, age, sex):
        # self.name, self.age, self.sex：属性
        self.name = name
        self.age = age
        self.sex = sex

    # eat/sleep/work:人的行为
    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')

    def work(self):
        print('工作')

# 类已经声明完了，可以根据类来创建对象。
# 创建张三这个对象
zhangsan = People('张三', '20', '男')
print(zhangsan.name)
print(zhangsan.age)
print(zhangsan.sex)
zhangsan.eat()
zhangsan.sleep()
zhangsan.work()
# 创建李四这个对象
lisi = People('李四', '30', '女')
print(lisi.name)
print(lisi.age)
print(lisi.sex)
lisi.eat()
lisi.sleep()
lisi.work()







