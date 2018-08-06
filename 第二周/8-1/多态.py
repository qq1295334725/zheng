"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:多态.PY
@ide:PyCharm
@time:2018-08-01 10:57:23
"""
# 多态：不同的子类对象调用相同的父类方法会产生不同的结果。
class Dog(object):
    def work(self):
        pass
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')
class DrugDog(Dog):
    def work(self):
        print('追查毒品')
class SearchDog(Dog):
    def work(self):
        print('搜救')
def dog_work(obj):
    obj.work()

dog1 = ArmyDog()
dog2 = DrugDog()
dog3 = SearchDog()
# dog1.work()

dog_work(dog1)
dog_work(dog2)
dog_work(dog3)


