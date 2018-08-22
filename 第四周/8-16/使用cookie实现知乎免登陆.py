"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用cookie实现知乎免登陆.PY
@ide:PyCharm
@time:2018-08-16 14:37:50
"""
import requests
session = requests.session()
headers = {
    "User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Host":"www.zhihu.com",
    "Cookie":'_zap=37e09260-20de-445d-856e-ebe421b15f10; _xsrf=Gzqpkwk0lisW5D0u8oo7BKrH3XOBJKW4; q_c1=1e98370745ee4df496d6323ce6d4e370|1534400495000|1534400495000; d_c0="AGBmnQttEA6PTmWKACbkhsQvOFW0JAKqcKA=|1534400495"; capsion_ticket="2|1:0|10:1534400496|14:capsion_ticket|44:YTE0ZmMyODFkYjRjNDRlY2I1M2RlOGY3M2I0NTZjMTk=|db73abaa859585e1f668da4eb67ca5a21cc35c9539078e742f4b0a695739e890"; z_c0="2|1:0|10:1534400702|4:z_c0|92:Mi4xMmUyZ0N3QUFBQUFBWUdhZEMyMFFEaVlBQUFCZ0FsVk52bVppWEFBX2FOQWpoYWxudklpNV9mbC1RRS1RZzg1c2NR|024c8a606cc6e6406845faeaf7100a3db655cbd571272b838dbfbbf089255ff0"; tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027'
}
# session.get("https://www.zhihu.com/")
response = session.get("https://www.zhihu.com/explore",headers=headers).text
print(response)























