"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:1111.PY
@ide:PyCharm
@time:2018-08-14 15:02:27
"""

import requests
from urllib.parse import urlencode
import re
class ChouTi(object):
    post_url = "https://dig.chouti.com/login"
    post_data = urlencode({"oneMonth":"1","password":"202325","phone":"8613525517200"})
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0)",
        "Cookie":"gpsd=44f7a6dabfd2aa1332523e399206851c; gpid=fd8304b29fb545c996835f3d1af5abde; puid=8b6a04795a7ae2d8dec34e2c5b9c09e1; JSESSIONID=aaaJwzFdpAL5l5W2GFxuw"
    }
    session = requests.Session()

    #登录
    def post_chou_ti(self):
        response = self.session.get('https://dig.chouti.com/',data=self.post_data,headers=self.headers).text
        # print(response)
        pattern_obj=re.compile(r'<div class="news-pic"><img lang="(.*?)"',re.S)
        id = re.findall(pattern_obj, response)
        # print(id)
        self.dian_zan(id)
    # 点赞
    def dian_zan(self,id):
        for yong_hu_id in id:
            url_base = 'https://dig.chouti.com/link/vote?linksId='+yong_hu_id
            self.session.post(url_base,headers=self.headers)
            print("点赞成功！")
if __name__ == '__main__':
    chouti = ChouTi()
    chouti.post_chou_ti()






















