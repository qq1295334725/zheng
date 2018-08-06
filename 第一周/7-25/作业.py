"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:作业.PY
@ide:PyCharm
@time:2018-07-25 19:51:50
"""

# 1.利用map()和reduce()函数，实现类似于int()的功能。比如:'123'-123
from functools import reduce
res1 = reduce(lambda x,y:x+y,'123')
res2 = map(int,res1)
for res3 in res2:
    print(res3,end='')
print('')
# 2.利用map()实现类似于字符串的lower()函数的功能。比如将AbCdEF全部转换成小写
def lower_string(string):
    if string.islower():
        return string
    else:
        return string.lower()
res4 = map(lower_string, input('请输入要转换成小写的字符：'))
for res5 in res4:
    print(res5,end='')



