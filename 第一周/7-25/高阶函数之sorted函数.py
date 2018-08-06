"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:高阶函数之sorted函数.PY
@ide:PyCharm
@time:2018-07-25 10:52:02
"""
# sorted()：用于对一个序列进行升序排列，，第一个参数：序列，第二个参数key：用于指定一个只接收一个参数的函数，这个函数用于从序列中的每个元素中提取一个用于排列的关键字，默认值是None。第三参数是reverse：有两个值，一个为True，一个为False，如果reverse=True，则列表中的元素会被倒序排列。
# sorted只是单纯的对列表内部排序，并没有返回值
from functools import  cmp_to_key
# sorted()默认按照ASCII码排序

list1 = [30, 50, 70, 3, 9]
list2 = sorted(list1)
print('排列之后的结果',list2)

list3 = sorted(list1, reverse = True)
print('倒序排列', list3)

#ASCII码，a=97，b=98,c=99,d=100
list4 = ['c','d','b','a']
list444 = sorted(list4, reverse = True)
print(list444)


list5 = [('b',4),('a',5),('c',2),('d',3)]
list6 = sorted(list5,key=lambda x:x[0])
print('=====',list6)

# 如何使用sorted（）函数实现对一个序列的降序排列
list7 = [20,15,70,3,9]
list8 = sorted(list7)
print('生序排列',list8)

# 如果X>Y返回-1，x<y返回1，是按照降序排列的
#如果x>y返回1，x<y返回-1，则就是默认的升序排列
def reversed(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
result = sorted(list7, key=cmp_to_key(reversed))
print(result)



print('****************************')
# 面试中的常考题：sort和sorted的区别
# sort:排序会改变原有的list，，而sorted排序只是对列表进行排序返回了一个新的经过排序之后的列表，并不会对原有的列表进行改动。
# sorted用于对一个序列进行排序，而sort只能用于列表的排序。
list9=[9, 5, 3, 8, 7, 1]
print(list9)
list12 = list9.sort()
print(list9)
print(list12,'=======')#None =======


print('------------------------')

list10 = [11, 15, 9, 7, 6]
list11 = sorted(list10)
print('list10是', list10)
print('list11是', list11)
print(list10)


test = (1, 2, 5, 9, 8)
# test.sort()#不能对元组排序
print(sorted(test))

