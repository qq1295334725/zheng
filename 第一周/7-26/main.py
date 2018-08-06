"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-25
@author:Mr.Zhang
@file:main.PY
@ide:PyCharm
@time:2018-07-25 16:40:30
"""
#import本质：相当于先把my_module这个模块中的所有代码先解释执行一遍，然后赋值给my_module这个变量。最后通过这个变量调用my_module里面的name，say_hello()
# import my_module
# my_module.say_hello()
# print(my_module.name)
# my_module.say_hello()

#from...import....本质：相当于把my_module里面的age，say_haha先放到main文件中执行一遍。所以就可以直接使用。
# from my_module import age,say_haha
# print(age)
# say_haha()

# from my_module import *
#
# def say_haha():
#     print('这是main里面的say_haha')
# print(age)
# print(name)
# say_hello()
# say_haha()
# from my_module import say_haha as say_haha_one
# say_haha()
# say_haha_one()


#当被导入模块中存在__all___=[]，则使用from 模块名 import * 这种方式进行导入的时候，只能导入__all__=[]里面定义的变量或者函数。
# from  my_module import *
# say_hello()
# print(name)
# say_haha()
# print(age)

# 导入包了的本质，执行包里的__init__.py文件里面的代码，
import package_test


# import sys
# print(sys.path)
# from package_test import my_module2
# print(my_module2.sex)
# my_module2.say_heihei()


from package_test.package_test1 import my_module3
print(my_module3.weight)
my_module3.say_xixi()







