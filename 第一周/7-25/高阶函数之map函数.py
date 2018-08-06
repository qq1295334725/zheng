"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:高阶函数之map函数.PY
@ide:PyCharm
@time:2018-07-25 09:04:01
"""
# map()函数：接受两个参数，一个是函数，一个是序列，map函数将序列中的每一个元素都传入函数中进行运算，并把结果当做一个迭代器进行返回。
def calc(x):
    res = x*x
    return res
# 计算；列表中每个元素的平方
result = map(calc,[1,2,3,4,5,6])
print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# for res in result:#遍历
#     print(res)
result = list(result)
print(result)

# 将列表中的每一个元素都转换成字符串
result1 = map(str,[1,2,3,4,5,6])
print(result1)
# print(type(next(result1)))
# print(next(result1))
# 可以用for循环遍历
# for res in result1:
#     print(type(res))
#     print(res)


# 将列表中的每一个元素都转换成整数
result_2 = map(int,('1','2','3','4','5','6'))
print(result_2)
# print(next(result_2))
# print(next(result_2))
# for res in result_2:
#     print(type(res))
#     print(res)

# 将字符串中的每一个元素都转换成整数
result_3 = map(int,'1234567')
print(result_3)
for res in result_3:
    print(type(res))
    print(res)


