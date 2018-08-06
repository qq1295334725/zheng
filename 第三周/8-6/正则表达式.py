"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:正则表达式.PY
@ide:PyCharm
@time:2018-08-06 16:29:34
"""
import re
# 正则表达式：是对字符串的内容进行匹配查询的一种方式，通过预先定义的一些特殊字符的组合，形成一种字符串的匹配规则，再根据这些规则来对字符串中的某一些内容进行提取或者查找。
# 常用的正则表达式转义字符：
'''
\d:匹配一个数字
\w:用于匹配一个数字或者字母
.:可以匹配前面字符后面跟着的任意一个字符。a.:可以匹配到ab,ac,ad
*:可以匹配前面字符0个或者多个。a*：可以匹配到0个或者,aa,aaa,aaaa.......
?:可以匹配到前面字符0个或者1个。a?:可以匹配到0个a,或者1个a
+:可以匹配前面字符任意多个，但是至少为1个，不能为0个。a+：a,aaaa,aaaaaa但是不能一个都匹配不到
^:表示必须以xxx字符开头。^a:只能匹配到以a开头的字符。
$：表示必须以某某字符结尾。a$:只能匹配到以a结尾的字符(a)
.*:这个组合表示任意字符出现0个或者多个，也称之为贪婪匹配模式，就是尽可能的匹配符合要求的最大值。a.*b可以匹配到ab,adb,a45dffb........
.*?:这个组合是非贪婪匹配模式，在能匹配成功的前提下，尽可能的少的匹配符合要求的字符。
.+:表示任意字符至少出现一次，不能为0次。a.+b:ab(匹配不到,中间没有其他字符),acb,addsb.....
|:用于设置不同情况的正则表达式，表示或者
'''
# 目标字符串：123456abcedfg
# 1.创建正则表达式对象.compile():括号里填写的字符串的匹配规则
# ():表示从目标字符串中提取的字串，一个（）对应着一个分组信息。
pattern_obj = re.compile('(\d+)(\w+)')
# 2.根据正则表达式对象，从目标字符串进行匹配。
# match():第一个参数，正则表达式对象，第二个对象：目标字符串,从头开始匹配。
res = re.match(pattern_obj,'123456abcdefg')
print(res.group(1))#str123456
print(res.group(2))

pattern_obj = re.compile('(c.)')
res = re.match(pattern_obj,'cbdefg')
print(res.group(1))

pattern_obj = re.compile('(a*)')
res = re.match(pattern_obj,'aaaaaaabcdefg')
print(res.group(1))

pattern_obj = re.compile('(a?)')
res = re.match(pattern_obj,'aaabcdefg')
print(res.group(1))

pattern_obj = re.compile('(b+)')
res = re.match(pattern_obj,'bbbbcdefg')
print(res.group(1))

pattern_obj=re.compile('(^cde)')
res = re.match(pattern_obj,'cdefgh')
print(res.group(1))

# match从头开始找，d$是以d结尾的，所有只能有d一个字符
pattern_obj = re.compile('(d$)')
res = re.match(pattern_obj,'d')
print(res.group(1))

pattern_obj = re.compile('(a.*b)')
res = re.match(pattern_obj,'afd45bbbbb4w54eb')
print(res.group(1))

pattern_obj = re.compile('(a.*?b)')
res = re.match(pattern_obj,'afd45bbbbb4w54eb')
print(res.group(1))

pattern_obj = re.compile('(a.+b)')
res = re.match(pattern_obj,'afd45bbbbb4w54eb')
print(res.group(1))

pattern_obj = re.compile('((haha|heihei)123)')
res = re.match(pattern_obj,'heihei123')
res1 = re.match(pattern_obj,'haha123')
print(res.group(1))
print(res.group(2))
print(res1.group(1))
print(res1.group(2))