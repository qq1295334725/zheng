"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用selenium模拟登陆百度云网盘并上传文件.PY
@ide:PyCharm
@time:2018-08-28 15:53:20
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://pan.baidu.com")
driver.implicitly_wait(5)
time.sleep(3)
# 等待三秒钟定位到账号密码登陆这个地方，进行点击
driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
time.sleep(3)
# 定位到账号输入框这个地方，进行点击
username_input = driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("17329406060")
time.sleep(3)
# 等待三秒钟定位到密码输入框这个地方，进行点击
password_input = driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("llCHEN@06.23.")
time.sleep(3)
code = input("请输入验证码：")
code_input = driver.find_element_by_id("TANGRAM__PSP_4__verifyCode").send_keys(code)
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
# 登陆成功
time.sleep(3)
upload_input = driver.find_element_by_id("h5Input0").send_keys("C:/Users/Administrator/Desktop/正课/第六周/8-28/text.text")
# 如果想操作本地窗口，可以autoit完成。








