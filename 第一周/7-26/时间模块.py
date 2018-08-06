"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-26
@author:Mr.Chen
@file:时间模块.PY
@ide:PyCharm
@time:2018-07-26 10:52:01
"""
import time

# 1.获取时间戳，时间戳是个单位为秒，从1970年1月1日00:00到现在一共经历的时间为多少秒。
# 时间戳一般用于验证登录是否过期。
timetamp = time.time()
print(timetamp)
# 2.localtime():用于获取本地时间的函数，返回值是一个元组
localtime = time.localtime()
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
# 3.asctime():获取格式化的本地时间
local_time = time.asctime(time.localtime())
print(local_time)
# 4.将本地时间元组格式化成2018-7-26 11:01：xx的形式
# strftime（）：将时间元祖转换成格式化的时间字符串
time_1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time_1)
# 5.将格式化的字符串转换成时间元组
string = 'Thu Jul 26 14:04 2018'
time_2 = time.strptime(string,'%a %b %d %H:%M %Y')
print(time_2)

string1= '2018-07-26 14:20:55'
time_3 = time.strptime(string1, '%Y-%m-%d %H:%M:%S')
print(time_3)

# 2018-7-26 14:04 Thu Jul
string2 = '2018-7-26 14:04 Thu Jul'
time_4 = time.strptime(string2, '%Y-%m-%d %H:%M %a %b')
print(time_4)

# 将时间元组转换成格式化的字符串：14:05:30 7-26-18
time_5 = time.strftime('%H:%M:%S %m-%d-%y',time.localtime())
print(time_5)

'''
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	一年中的第几天，1 到 366
8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1 
'''

'''

    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
'''

