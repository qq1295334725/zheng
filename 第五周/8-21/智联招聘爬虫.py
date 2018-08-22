"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:智联招聘爬虫.PY
@ide:PyCharm
@time:2018-08-21 09:46:47
"""
import urllib.request
import re
import xlwt
from fake_useragent import UserAgent
from urllib.parse import quote
class ZLZP(object):
    def __init__(self,work_name,work_place):
        self.work_name = work_name
        self.work_place = work_place
        self.ua = UserAgent()
        # ie的浏览器标识，ua.ie
        # opera浏览器标识 ua.opera
        # chrome浏览器标识  ua.chrome
        # firefox浏览器标识  ua.firefox
        # safri浏览器标识  ua.safri
        # 随机浏览器标识  ua.random
        self.headers = {
            'User-Agent':self.ua.ie,
            'Cookie':'urlfrom=121113803; urlfrom2=121113803; adfcid=pzzhubiaoti; adfcid2=pzzhubiaoti; adfbid=0; adfbid2=0; dywea=95841923.2942264507928802300.1534817261.1534817261.1534817261.1; dyweb=95841923.17.9.1534817490314; dywec=95841923; dywez=95841923.1534817261.1.1.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; ZP_OLD_FLAG=true; __xsptplus30=30.1.1534817262.1534817537.3%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23PXLLoBfWsSCPpC-uSbLjqf3ZI3uxFlCN%23; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1534817262; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1534817282; sts_deviceid=1655a3cdb0a9-04c6d189846b748-47504133-2073600-1655a3cdb0b54; sts_sg=1; sts_evtseq=9; sts_sid=1655a3cdb0ea3-095e7c83418c968-47504133-2073600-1655a3cdb0f1d; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAhw9s0P7KI0KqiAsjhTLVU00000FxNENb000008Tsaq1.THLyktAJdIjA80K85ydEUhkGUhNxndqbusK15H6kPjnzPy7Bnj0snH01mhR0IHY3wWwjnjPDfYfLrH-jPRR3nRcYf1c1nHwKrHRvfWcvn0K95gTqFhdWpyfqn1D1nW6kPHTYnzusThqbpyfqnHm0uHdCIZwsrBtEILILQMGCmyqspy38mvqV5LPGujYknWDknHn3njnhTv-YuHdsXMGCIyFGmyqYpfKWThnqPHn4njT%26tpl%3Dtpl_11535_17772_13457%26l%3D1505613207%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3132815743_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D83%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26rqlang%3Dcn; ZP-ENV-FLAG=gray; GUID=e5299bc69bd14d1aacf3e8f39729a005; ZL_REPORT_GLOBAL={%22sou%22:{%22actionIdFromSou%22:%220539f04a-18ce-4886-acc8-1961a3840460-sou%22%2C%22funczone%22:%22smart_matching%22}}; LastCity=%E9%83%91%E5%B7%9E; LastCity%5Fid=719; Hm_lvt_d838d7d6abb840b6c1a339ec5aee915d=1534817282; Hm_lpvt_d838d7d6abb840b6c1a339ec5aee915d=1534817282; _jzqa=1.3454043793398008300.1534817295.1534817295.1534817295.1; _jzqb=1.5.10.1534817295.1; _jzqc=1; _jzqx=1.1534817295.1534817295.1.jzqsr=ts%2Ezhaopin%2Ecom|jzqct=/jump/index_new%2Ehtml.-; _jzqckmp=1; _qzja=1.1306452558.1534817295525.1534817295525.1534817295525.1534817295525.1534817605453.0.0.0.2.1; _qzjb=1.1534817295525.2.0.0.0; _qzjc=1; _qzjto=2.1.0; qrcodekey=ea4cfcb37cf1412b8f379cb4d66b222b; lastchannelurl=https%3A//passport.zhaopin.com/findPassword/mobile/step2%3Freceiver%3D13525517200; firstchannelurl=https%3A//passport.zhaopin.com/account/login%3FbkUrl%3Dhttps%253A//sou.zhaopin.com/%26y7bRbP%3Ddpour7HkaZHkaZHkuw6fRAkTK_C1iVXwVTK_WMnw8ZW; JsNewlogin=3009569039; JSloginnamecookie=13525517200; JSShowname=13525517200; at=769911b2ac8e4008b75002de3ccbc167; Token=769911b2ac8e4008b75002de3ccbc167; rt=0b219b2c1604431f8ead84f9f9d39a4f; JSsUserInfo=3e692f645b6a5864436b596b57665b695c7352695d64516a5064486b256b2a665769557358695e64546a5c64466b586b5366586954735b695064356a3d644e6b586b5f662b69307356695c644b6a5b64536b586b54665069557359695064276a25644e6b596b5f663f692573566921642f6a5964406b586b5c66536952735c695264526a5264266b3d6b59665b695f73386922645b6a5c64436b596b55665a6950735a695064336a39643d6b546b55665969517359695e64536a5864446b5b6b54665a695f734; uiioit=213671340f69446b5d6a5879476442740e350d325f755c6d5368427426733036083402694e6b8; dywem=95841923.y; usermob=5075446853695A645C755B765A6142775A66596854698; userphoto=; userwork=0; bindmob=1; monitorlogin=Y; loginreleased=1'
        }
        self.base_url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&sm=0&p=1'.format(quote(self.work_place),quote(self.work_name))
        self.page_num = 1
        self.record_row = 1

    # 定义一个函数来获取网页的源代码
    def get_page_code(self,url,sheet):
        '''

        :param url:传入的是每一页的地址
        :return:
        '''
        request = urllib.request.Request(url,headers=self.headers)
        try:
            response = urllib.request.urlopen(request)
        except Exception as e:
            print('页面获取失败，原因是：',e)
        else:
            print('正在爬取第{}页数据，请稍候...'.format(self.page_num))
            html=response.read().decode('utf-8')
            # 将html传到用来解析的函数当中用来解析
            new_list = self.get_all_data(html)
            # 将new_list传入到
            self.write_data(new_list,sheet)
            self.page_num += 1
            # 获取下一页的url
            self.get_next_url(html,sheet)
    # 定义一个函数来解析页面的源代码
    def get_all_data(self,html):
        '''
        用来解析的源代码
        :return:每一页的源代码
        '''
        pattern = re.compile(r'<a style="font-weight: bold".*?</b>(.*?)</a>.*?<span>(.*?)</span>.*?"_blank">(.*?)</a>.*?"zwyx">(.*?)</td>.*?"gzdd">(.*?)</td>',re.S)
        result_list = re.findall(pattern,html)
        # print(result_list)
        remove_b = re.compile("<b>")
        remove_b1 = re.compile("</b>")
        remove_a = re.compile('(&nbsp.*?middle">)')
        new_list=[]
        for result in result_list:
            job_name=re.sub(remove_b,'',result[0])
            job_name=re.sub(remove_b1,'',job_name)
            if "&nbsp" in job_name:
                job_name = re.sub(remove_a,'',job_name)
            result_tuple=(job_name,result[1],result[2],result[3],result[4])
            new_list.append(result_tuple)
        return new_list

    def open_excel_file(self):
        # 创建工作表对象
        work_book = xlwt.Workbook(encoding='utf-8')
        # 设置工作表名称
        sheet = work_book.add_sheet("%s职位表"%self.work_name)
        # 设置表头
        sheet.write(0, 0, "工作名称")
        sheet.write(0, 1, "反馈率")
        sheet.write(0, 2, "公司名称")
        sheet.write(0, 3, "薪资")
        sheet.write(0, 4, "工作地点")
        return work_book,sheet

    def write_data(self, new_list,sheet):
        for gzmc,fkl,gsmc,xz,gzdd in new_list:
            sheet.write(self.record_row,0,gzmc)
            sheet.write(self.record_row,1,fkl)
            sheet.write(self.record_row,2,gsmc)
            sheet.write(self.record_row,3,xz)
            sheet.write(self.record_row,4,gzdd)
            # 每写入一行都需要将行数加1，才能将数据写入到下一行
            self.record_row += 1

    # 获取下一页的地址
    def get_next_url(self,html,sheet):
        pattern_obj = re.compile(r'<li class="pagesDown-pos">.*?href="(.*?)"',re.S)
        try:
            res = re.search(pattern_obj, html)[1]
            # print(res)
        except Exception as e:
            print('没有下一页了',e)
        else:
            next_page_url = res
            self.get_page_code(next_page_url,sheet)
    # 启动函数
    def start_spider(self):
        workbook,sheet = self.open_excel_file()
        self.get_page_code(self.base_url,sheet)
        workbook.save("%s+%s职位表.xls"%(self.work_place,self.work_name))


if __name__ == '__main__':
    s = ZLZP('Python','郑州')
    s.start_spider()


