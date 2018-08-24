"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用zmail发送邮件.PY
@ide:PyCharm
@time:2018-08-23 17:13:44
"""
import zmail
# 设置邮件内容
mail_content = {
    "subject":"上次那个文件",
    # "content":"恭喜老总喜提兰博基尼"
    # "content":"欢迎光临智游官网http://www.zhiyou100.com",
    # 发送附件
    # 如果要发送的文件不在当前目录里，则使用绝对路径。
    "attachments":["xici(1).txt","6565656.jpg","shangseqiu.txt"]
}
try:
    # 第一个参数：邮箱账号，第二个参数：授权码
    server=zmail.server("13525517200@163.com","llchen0623")
    # 发送邮件，第一个参数：收件人地址，第二个参数：要发送的内容
    # server.send_mail("1295334725@qq.com", mail_content)
    server.send_mail(["1295334725@qq.com","791063894@qq.com"], mail_content)
except Exception as e:
    print("发送失败，原因是：",e)
else:
    print("发送成功！")













