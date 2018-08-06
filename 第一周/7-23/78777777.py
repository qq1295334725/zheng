"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:78777777.PY
@ide:PyCharm
@time:2018-07-28 09:22:52
"""
'''
import 模块名
form 模块名 import 变量1，变量2，函数1，函数2
form 模块名 import *
from mo import  XX as qq
'''
def result(list1):
    return list1%2==1
res = filter(result, [1,2,3,4,5,6,7])
for x in res:
    print(x)

res2 = filter(lambda number:number%2==1,[1, 2, 3 ,4, 5, 6, 7])
for x in res2:
    print(x)

res3 = filter(lambda num:num.islower(),'DFfgEds')
for x in res3:
    print(x)

from functools import reduce
def add(x,y):
    return x+y
res4 = reduce(add,[1,2,3,4,5,6])
print(res4)

res5 = reduce(lambda x,y:x+y,[1,2,3,4,5,6])
print(res5)

res6 = sorted('agd',reverse=False)
print(res6)
res7 = sorted([('a',2),('d',4),('b',1)],key=lambda x:x[1],reverse=True)
print(res7)

