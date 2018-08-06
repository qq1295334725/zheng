"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:00.PY
@ide:PyCharm
@time:2018-07-23 16:38:34
"""
x=3==3,5#x=(3==3,5)
print(x)


def res(choose_num):
    # choose_num = input('请输入选择：')
    while choose_num>2 or choose_num<1:
        raise Exception('cuowu')
    if choose_num == 1:
        pass
    if choose_num == 2:
        pass
try:
    res1 = res(3)
except Exception as e:
    print('错误原因是：',e)
else:
    print('输入正确！')
finally:
    print('结束')

res2 = lambda :print('===')
res2()


