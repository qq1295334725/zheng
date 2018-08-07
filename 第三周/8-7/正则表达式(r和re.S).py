"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:正则表达式(r和re.S).PY
@ide:PyCharm
@time:2018-08-07 09:29:51
"""
import re
# r'':一般用在正则表达式中，称之为原始字符串，作用是将python语法中的反斜杠转义给取消，将其置换成一个普通的字符串，可以解决python中转义字符产生的问题。
# \n：在python中代表换行符，起换行作用。
print('a\nb')
print(r'a\nb')
# \b:在python中表示退格的作用。
print('123\b456')
# \b:在正则表达式中表示的匹配边界位置。
pattern_obj = re.compile(r'\bword\b')
res = re.search(pattern_obj,'abc word 123')
print(res[0])

# re.S:作用是将字符串中的换行符当做一个普通的字符来处理，让正则表达式匹配的时候不受到换行符的影响，把所有行的字符串都看成一个整体来处理。
string = '''my name is
heihei your name is
haha
'''
pattern_obj = re.compile(r'my(.*?)haha',re.S)
res = re.search(pattern_obj,string)
print(res[0])
# 默认情况下，正则表达式在使用search和match匹配的时候，是按照整行内容进行匹配的，如果在当前行没有匹配成功，则切换到下一行继续进行匹配。

# match,search取括号里的
# 如果括号里是1的话，res和geoup都有my和haha,如果是0都没有

