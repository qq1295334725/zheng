"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-26
@author:Mr.Chen
@file:datetime.PY
@ide:PyCharm
@time:2018-07-26 14:34:55
"""
import datetime
# 1.获取当前时间和日期
datetime_dt = datetime.datetime.today()
print('当前时间和日期是：{}'.format(datetime_dt))

# 格式化日期和时间
datetime_str = datetime_dt.strftime('%Y-%m-%d %H:%M:%S')
print('当前时间和日期格式化之后为:{}'.format(datetime_str))

# 3.设置时间间隔
time_delta = datetime.timedelta(hours=3)
print('当前设置的时间间隔为：{}'.format(time_delta))
# 把当前的时间往后延迟三个小时
datetime_pre = datetime.datetime.today()+time_delta
print('时间延后三个小时为：{}'.format(datetime_pre))

# 4.获取当前日期
date = datetime.datetime.today().date()
print('当前日期为：{}'.format(date))
# 5.获取当前时间
time = datetime.datetime.today().time()
print('当前时间为：{}'.format(time))

# 6.将时间和日期转换为时间戳
time_a = datetime.datetime.today().timestamp()
print('现在的时间戳为：{}'.format(time_a))
