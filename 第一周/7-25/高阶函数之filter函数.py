"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:高阶函数之filter函数.PY
@ide:PyCharm
@time:2018-07-25 09:23:13
"""
# filter():用于对一个序列进行过滤或筛选。
# 两个参数：第一个参数：函数，用于设置过滤的逻辑；第二个参数：序列
# 返回值是个迭代器。

# 定义一个函数，用于过滤奇偶数
def filter_funcition(number):
    return number%2 == 3
# filter()函数会将序列中的每一个元素都传递到函数中执行，在函数中返回True或者False，filter（）函数会根据返回的结果，保留True的元素，过滤False的元素。
result = filter(filter_funcition,[1,2,3,4,5,6])
print(result)
for res in result:
    print(res)

# 将字符串中的大写的字符过滤掉。
# 定义一个过滤函数
def filter_upper_char(string):
    return string.islower()

result_1 = filter(filter_upper_char,'AbcDewQ')
print(result_1)
for res in result_1:
    print(res)

# 使用lambda函数改造：
result_3 = filter(lambda number:number%2==1,[1,2,3,4,5,6,])
print(result_3)
for res in result_3:
    print(res)

result_4 = filter(lambda  string:string.islower(),'AbcDewQ')
print(result_4)
for res1 in result_4:
    print(res1)







