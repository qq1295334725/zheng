"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:高阶函数之reduce函数.PY
@ide:PyCharm
@time:2018-07-25 10:00:12
"""
from functools import reduce
# reduce():接收两个参数，第一个参数：函数，第二个参数：序列。
# 作用：将序列中的前两个元素进行一次运算，然后运算结果再和第三个元素进行运算.

def add(x, y):
    res = x + y
    return res
result = reduce(add, ['a', 'b', 'c', 'd'])
print(result)
# 第一次运算结果：ab  #在字符串中add是将字符串拼接
# 第二次运算结果：abc
# 第三次运算结果：abcd

result1 = reduce(add, [1, 2, 3, 4])
print(result1)


# 使用lambda改造。
result2 = reduce(lambda x,y:x+y,['a','b','c','d'])
print(result2)






