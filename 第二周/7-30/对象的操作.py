"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:对象的操作.PY
@ide:PyCharm
@time:2018-07-30 11:20:58
"""
class People(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def sleep(self):
        print('睡觉')

    def eat(self):
        print('吃饭')

    def work(self):
        print('工作')
p1=People('p1','20','男')
p2=People('p2','30','女')
#动态给某一个对象添加属性weight
p1.weight='180'
print(p1.weight)
#hasattr():判断某个对象是否有某个属性
#hasattr('对象名','属性名')，该函数返回的是个bool值。
if hasattr(p2,'weight'):
    print(p2.weight)
else:
    print('p2没有weight这个属性')
#getattr():用于获取某一个对象的属性值
#getattr('对象名','属性名','属性默认值')：当获取的属性存在的时候，则直接获取属性值。如果属性不存在，则返回属性默认值，防止报错。
print(getattr(p1,'height','100'))
#setattr():用于给某一个对象添加一个属性值
#setattr('对象名','属性名’，'默认值'):当添加的属性不存在的时候，则会给该对象添加一个属性名和默认的属性值。如果已经存在，则会修改该对象的属性值。

setattr(p2,'color','black')
print(p2.color)
setattr(p2,'age','35')
print(p2.age)

#delattr('对象名'，'属性名'):用于删除某一个对象的属性
delattr(p2,'color')
try:
    print(p2.color)
except:
    print('有错误')





