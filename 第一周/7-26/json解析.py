"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-26
@author:Mr.Chen
@file:json解析.PY
@ide:PyCharm
@time:2018-07-26 16:06:28
"""
# pip install requests  #cmd中安装包
# 第三方的用于发送网络请求的一个模块，经常被用于爬虫
import requests
import json
response = requests.get('http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?').text
print(type(response))
print(response)
res_result = json.loads(response)
print(res_result)
# 取error的值
error = res_result['error']
print('error的值',error)
# 取status的值
status = res_result['status']
print(status)
# 取date的值
date = res_result['date']
print(date)
# 取result的值:取出来的结果是一个列表，列表里包含着一个字典
results = res_result['results']
print(results)
# 从results这个列表中取出来这个字典
dict_1 = results[0]
print(type(dict_1))
print(dict_1)
# 从dict_1这个字典中，通过键取值
currentCity = dict_1['currentCity']
print(currentCity)
pm_25 = dict_1['pm25']
print(pm_25)
# 从 dict_1这个字典中取出键是index的值，对应的是一个列表
index = dict_1['index']
print('========',index)

# 使用for循环遍历index这个列表
for dex in index:
    # 取出来的每一个dex都是一个字典
    des = dex['des']
    tipt = dex['tipt']
    title = dex['title']
    # zs = dex['zs']
    print(des, tipt, title)

weather_data = dict_1['weather_data']
print(weather_data)
for res in weather_data:
    date = res['date']
    dayPictureUrl = res['dayPictureUrl']
    nightPictureUrl = res['nightPictureUrl']
    weather = res['weather']
    wind = res['wind']
    temperature = res['temperature']
    print(date, dayPictureUrl, nightPictureUrl, weather, wind, temperature)








