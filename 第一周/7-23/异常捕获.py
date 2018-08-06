"""
座右铭:将来的你一定会感激现在拼命的自己
@project:预科
@author:Mr.Chen
@file:异常捕获.PY
@ide:PyCharm
@time:2018-07-23 15:43:46
"""
# try....except....:用于捕获代码异常，当一段程序出现异常的时候，会导致程序崩溃，整个程序会结束运行，后续的代码程序的一些代码逻辑也不会在执行，但是当异常捕获并进行处理，可以保证整个程序的正常执行，后续的代码也不会受到异常的影响。

try:
    # 写要捕获异常的代码
    pass
except Exception as e:
    # Exception:异常类，基本上能捕获常见的异常情况，表示异常原因
    # e，用于接收错误原因的。
    pass
    # 出现异常时，需要设置的代码逻辑
    # 当try里面的代码执行成功的时候，则不会执行except Exception as e里面的代码
else:
    pass
    # 如果try里面的代码执行成功，则紧接着会执行else中的代码
    # 如果try出现异常，没有执行成功，则不会执行else里面的代码
finally:
    pass
    # 不管try执行成功还是失败，最终都会执行finally语句里的代码


# example:
list1 = [1]
try:
    print(list1[0])
except IndexError as e:
    print('try里面的代码出现异常没有执行成功，所以需要执行我！')
    print('错误的原因error：',e)
else:
    print('try里面的代码执行成功，则会接着执行我！try里面的代码没有执行成功，则不会执行我！')
finally:
    print('不管try执行成功还是失败，最终都会执行我！')


try:
    import a
except ImportError as e:
    print('错误的原因是error:',e)

# 在函数内部自定义一个异常：当调用该函数的时候，如果不符合函数内部定义的条件，则抛出这个异常！如果符合函数条件，就不抛出异常！
def is_outrange(age):
    if age<16:
        raise Exception('小于16周岁，不能谈恋爱！')
    else:
        return True
# res=is_outrange(15)
try:
    res=is_outrange(15)
except Exception as e:
    print('错误原因error：',e)


# 面试题中常问的问题：你遇到过的错误类有哪些？
# ImportError:导入错误
# IndexError:索引错误
# NameError:尝试访问一个没有声明的变量
# SyntaxError:语法错误
# AttributeError:尝试访问未知的对象属性
# KeyError:请求一个不存在的字典关键字
# ValueError:传给参数的参数类型不正确

