"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:类的单继承.PY
@ide:PyCharm
@time:2018-07-31 15:42:33
"""
#面向对象编程的三个基本特征：封装 继承 多态

#函数是封装的最基本单位，而类和对象属于更高级的封装形式。在类中封装属于用于保存数据，也可以在类中封装函数用于操作数据。不同的功能和逻辑又可以封装成不同的函数。


#继承：
#继承的优势:可以更好的实现代码的重用
#1.子类可以继承于父类，子类会拥有父类中所有的属性和函数，子类不需要重复声明。父类的对象是不能够调用子类的属性和方法的。这种继承属于单向继承。
#2.当父类当中的属性和函数不符合子类需求的时候，子类是可以重写父类的属性和方法的，或者自定义一些新的方法

#object：(根类，基类)是所有类的父类
#Animal类是object的子类，object是Animal的父类
#如果一个类没有特别指定父类，一般都是继承于Object
class Animal(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.__sex=sex
    def run(self):
        print('跑')
    def eat(self):
        print('吃')
    def __sleep(self):
        print('睡')

#声明一个狗类继承于Animal
class Dog(Animal):
    def wangwang(self):
        print('叫')

an=Animal('动物','20','公')
print(an.name)
print(an.age)
# print(an._Animal__sex)
an.run()
an.eat()
# an.wangwang()
#Dog类中，虽然并没有声明__init__这个初始化函数，但是由于Dog类继承于Animal类，所以，Dog类中的对象也去执行了Animale的初始化函数，在创建Dog类对象的时候，必须指定__init__函数中的实参。
dog=Dog('藏獒','8','母')
print(dog.name)
print(dog.age)
dog.run()
dog.eat()
dog.wangwang()
# print(dog._Dog__sex)
# dog._Dog__sleep()

#总结：
#1.私有属性，不能通过对象直接访问，但是可以通过设置方法(函数)访问
#2.父类中的私有属性，私有方法，不会被子类继承，也不能被访问(但是父类可以强制访问)。
#3.一般情况下，私有属性还有私有方法，是不可以被外部所访问的。(强制访问除外)



