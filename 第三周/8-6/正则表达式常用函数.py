"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:正则表达式常用函数.PY
@ide:PyCharm
@time:2018-08-06 17:37:10
"""
import re
# match():是从目标字符串的开头位置开始匹配，仅限于开头位置，匹配成功则返回match对象，否则返回None
pattern_obj = re.compile('(my)')
res = re.match(pattern_obj,'myhaha')
print(res.group(1))#my
# search():从目标字符串的任意位置开始匹配数据，仅匹配成功一次，如果目标字符串有多个符合要求的结果，也只能找到一个。
pattern_obj = re.compile('(my)')
res = re.search(pattern_obj,'heihiemyhahamy')
print(res.group(1))#my

pattern_obj = re.compile('my')
res = re.search(pattern_obj,'heihiemyhahamy')
print(res[0])#my

# findall():搜索整个目标字符串，会将所有匹配成功的字符串都返回出来。
pattern_obj = re.compile('(my)')
res = re.findall(pattern_obj,'heihiemyhahamy')
print('=====',res[0])#===== my
print('=============',res[1])#============= my
for x in res:
    print('---',x)#--- my  --- my

# splite():以匹配到的符合要求的字符串为分隔符，将目标字符串分割成一个列表。
pattern_obj = re.compile('my')
res = re.split(pattern_obj,'heihiemyhahamyhehe')
print('++++',res)#++++ ['heihie', 'haha', 'hehe']
# sub():使用一个新的字符来替换目标字符串中符合匹配要求的字符。
pattern_obj = re.compile('-')
res = re.sub(pattern_obj,'+','a-b-c')
print(res)#a+b+c




