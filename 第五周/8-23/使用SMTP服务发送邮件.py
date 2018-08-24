"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用SMTP服务发送邮件.PY
@ide:PyCharm
@time:2018-08-23 15:43:40
"""
# smtp:简单的邮件传输协议
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# 设置第三方smtp服务器地址
# 腾讯：smtp.qq.com,网易：smtp.163.com
mail_host = "smtp.163.com"
# 设置端口号
# 腾讯，465，网易：25
port = 25
# 设置用户名（腾讯@qq.com,网易@163.com）
mail_user = "13525517200@163.com"
# 设置授权码（腾讯的授权码系统分配的,前两个,第一个的授权码，，网易的是自己设置的）
mail_pass = "llchen0623"
# 设置发送人
sender = "13525517200@163.com"
# 设置收件人
receiver = "13525517200@163.com"
# 给多个人发送邮件
receiver_list=["13525517200@163.com","1295334725@qq.com"]



# 发送一封纯文本文件
def send_wenben():
    # 设置邮件标题
    subject = "嘤嘤嘤，咋不理人家呀"
    # 设置发送内容
    content = "信球你欠了我500万！今天的基金降了"
    # 第一个参数：发送的消息内容，必须是字符串
    # 第二个参数：要发送的信息内容的类型，默认plain，表示一个没有格式的纯文本内容
    # 第三个参数：编码方式，默认是ascii
    message = MIMEText(content, "plain", "utf-8")
    message["From"] = sender
    message["To"] = ",".join(receiver_list)
    message["Subject"] = subject
    try:
        # 网易的是SMTP（），腾讯的是SMTP_SSL()
        smtp_obj = smtplib.SMTP()
        # 连接第三方邮箱
        smtp_obj.connect(mail_host,port)
        # 登录自己的邮箱
        # 第一个参数：邮箱账号，第二个参数：邮箱授权码
        smtp_obj.login(mail_user,mail_pass)
        # 发送邮件
        smtp_obj.sendmail(sender,receiver,message.as_string())
        print('邮件发送成功！')
    except Exception as e:
        print("邮件发送失败，原因是：",e)

send_wenben()
# 发送一个html格式的文本
def send_html():

    # 设置邮件标题
    subject = "HTML文本测试"
    # 设置发送内容
    content = """
    <p>欢迎光临智游官网</p>
    <p><a href="http://www.zhiyou100.com">智游官网</a></p>
    """
    # 第一个参数：发送的消息内容，必须是字符串
    # 第二个参数：要发送的信息内容的类型，默认plain，表示一个没有格式的纯文本内容
    # 第三个参数：编码方式，默认是ascii
    message = MIMEText(content, "html", "utf-8")
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    try:
        # 网易的是SMTP（），腾讯的是SMTP_SSL()
        smtp_obj = smtplib.SMTP()
        # 连接第三方邮箱
        smtp_obj.connect(mail_host, port)
        # 登录自己的邮箱
        # 第一个参数：邮箱账号，第二个参数：邮箱授权码
        smtp_obj.login(mail_user, mail_pass)
        # 发送邮件
        smtp_obj.sendmail(sender, receiver, message.as_string())
        print('邮件发送成功！')
    except Exception as e:
        print("邮件发送失败，原因是：", e)
# send_html()


def send_fujian():
    subject = "7月的图片"

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    # 构建第一个附件，传送当前目录下的text.txt文件
    fujian_one=MIMEText(open("xici(1).txt","rb").read(),"base64","utf-8")
    fujian_one["Content-Type"]="application/octet-stream"
    # filename，可以随意设置，设置成什么名称，邮件中就会显示什么名称，最好和文本名保持一致
    fujian_one["Content-Disposition"]='attachment;filename="xici(1).txt"'

    # 构建第二个附件，传送当前目录下的6565656.jpg文件
    fujian_two = MIMEText(open("6565656.jpg", "rb").read(), "base64", "utf-8")
    fujian_two["Content-Type"] = "application/octet-stream"
    # filename，可以随意设置，设置成什么名称，邮件中就会显示什么名称，最好和文本名保持一致
    fujian_two["Content-Disposition"] = 'attachment;filename="6565656.jpg"'

    # 构建第三个附件，传送当前目录下的movie.csv文件
    fujian_three = MIMEText(open("6565656.jpg", "rb").read(), "base64", "utf-8")
    fujian_three["Content-Type"] = "application/octet-stream"
    # filename，可以随意设置，设置成什么名称，邮件中就会显示什么名称，最好和文本名保持一致
    fujian_three["Content-Disposition"] = 'attachment;filename="movie.csv"'
    message.attach(fujian_one)
    message.attach(fujian_two)
    # message.attach(fujian_three)

    try:
        # 网易的是SMTP（），腾讯的是SMTP_SSL()
        smtp_obj = smtplib.SMTP()
        # 连接第三方邮箱
        smtp_obj.connect(mail_host, port)
        # 登录自己的邮箱
        # 第一个参数：邮箱账号，第二个参数：邮箱授权码
        smtp_obj.login(mail_user, mail_pass)
        # 发送邮件
        smtp_obj.sendmail(sender, receiver, message.as_string())
        print('邮件发送成功！')
    except Exception as e:
        print("邮件发送失败，原因是：", e)

# send_fujian()






