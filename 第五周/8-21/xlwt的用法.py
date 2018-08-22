"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:xlwt的用法.PY
@ide:PyCharm
@time:2018-08-21 09:48:00
"""
import xlwt
# 创建一个工作表对象
workbook = xlwt.Workbook(encoding='utf-8')
# 设置excel表名
sheet = workbook.add_sheet('Python13期学生信息表')
# 往表格中填充数据
# 第一个参数表示行号，第二个参数表示列号
sheet.write(0,0,'姓名')
sheet.write(0,1,'年龄')
sheet.write(0,2,'身高')
sheet.write(0,3,'体重')

sheet.write(1,0,'张三')
sheet.write(1,1,'20')
sheet.write(1,2,'180')
sheet.write(1,3,'140')
workbook.save("学生信息表.xls")





