"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:main.PY
@ide:PyCharm
@time:2018-07-25 16:40:34
"""
# import本质，相当于先把my_module这个模块中的所有代码先解释执行一遍，然后赋值给 my_module这个变量，最后通过这个变量调用 my_module里面的 name,say_hello()
import my_module
# my_module.say_haha()
# print(my_module.name)
# my_module.say_hello()


# from...import...本质：相当于把 my_module里面的age，say_haha先放到main文件中执行一遍，所以就可以调用
# from my_module import  age,say_haha
# print(age)
# say_haha()


from my_module import *
#
# def say_haha():
#     print('这是main里面的haha')

# print(age)
# print(name)
# say_hello()
# say_haha()

# from my_module import say_haha as say_haha_one
# say_haha()
# say_haha_one()


# 当被导入模块中存在__all__=[],则使用from模块名  import *这种方式进行导入的时候，只能导入__all__=[]里面定义的函数或者变量。
# from my_module import *
# say_hello()
# print(name)
# say_haha()
# print(age)
