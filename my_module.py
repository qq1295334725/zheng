"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:my_module.PY
@ide:PyCharm
@time:2018-07-25 16:40:03
"""
__all__ = ['say_hello','name']

name='张三'
age = '21'

def say_hello():
    print('hello')
def say_haha():
    print('haha')
print('my_module里的print执行了')

if __name__ == '__main__':
    say_haha()
