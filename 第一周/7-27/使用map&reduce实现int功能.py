"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用map&reduce实现int功能.PY
@ide:PyCharm
@time:2018-07-27 09:24:06
"""
# 1.利用map()和reduce()函数，实现类似于int()的功能。比如:'123'-123
from functools import  reduce
# 字符串'123'转换成一个整数123
# 两个步骤：
# 第一步：先将字符串'123'中每一个字符'1','2','3'都转换成数字1,2,3.使用map函数
# 第二步：再讲每一个数字进行相应的处理，使其成为整数123,使用reduce函数

def char_to_number(string):
    all_number_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    # 以参数string为键，取出 all_number_dict里面的值
    return all_number_dict[string]
res = list(map(char_to_number, '123'))
print(res)

def result_number(x, y):
    res = x*10 + y
    return res
result = reduce(result_number, res)
print('最终的结果：',result,'最终的类型：',type(result))


# 整体进行封装一下，使其使用起来和int函数一样方便
def custom_int(s):
    def char_to_number(string):
        all_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        # 以参数string为键，取出 all_number_dict里面的值
        return all_number_dict[string]
    def result_number(x, y):
        res = x * 10 + y
        return res
    return reduce(result_number, map(char_to_number, s))

res = custom_int('456')
print(type(res))
print(res)