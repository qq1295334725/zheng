"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:454.PY
@ide:PyCharm
@time:2018-07-30 20:42:02
"""
# 1.利用map()和reduce()函数，实现类似于int()的功能。比如:'123'-123
from functools import reduce

# def number_int(reult):
#
#     all_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     num = all_number_dict[reult]
#
#     return num
#     # print(list1)
# res=list(map(number_int,'123'))
# # list2 = list1
# print(res)
# res1 = reduce(lambda x,y:x*10+y,[1,2,3])
# print(res1)


def result1(s):
    def int_str(string):
        all_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return all_number_dict[string]
    def int_num(x,y):
        res = x*10+y
        return res
    return reduce(int_num,map(int_str,s))
res2 = result1('123')
print(res2)











