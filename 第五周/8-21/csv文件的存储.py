"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:csv文件的存储.PY
@ide:PyCharm
@time:2018-08-21 14:48:27
"""
# csv（逗号分隔符），它是一种通用的文件格式，它可以非常轻易的被导入到各Excel表格或者数据库当中。csv文件，一行代表一条数据
import csv
# 将列表写入到csv文件当中
rows = [["张三","20"],['李四','25'],['麻子','26']]
# 使用上下文管理器
# with open('test1.csv', 'w', encoding='utf-8', newline='') as f:
#     # 通过csv模块创建一个用于写入数据的对象writer
#     writer = csv.writer(f)
#     writer.writerow(["姓名","年龄"])
#     for row in rows:
#         writer.writerow(row)
#
# with open('test2.csv', 'w', encoding='utf-8', newline='') as f:
#     # 通过csv模块创建一个用于写入数据的对象writer
#     writer = csv.writer(f)
#     writer.writerow(["姓名","年龄"])
#     writer.writerows(rows)


# 对列表的读取
with open("test1.csv", 'r', encoding='utf-8') as f:
    # 通过csv模块创建一个用于读取数据的对象reader
    reader = csv.reader(f)
    print(reader)
    for row in reader:
        print(row)

# csv文件对字典操作
# rows1 = [{"name":"张三","age":"20","sex":"男"},{"name":"小红","age":"22","sex":"女"},{"name":"王二","age":"19","sex":"男"},{"name":"小丽","age":"25","sex":"女"}]
#
# with open("test3.csv", "w", encoding='utf-8', newline='')as f:
#     keys = [key for key in rows1[0]]
#     # 创建一个用于写入字典数据的对象
#     # fildnames:是用来设置Excel表的表头
#     writer = csv.DictWriter(f, fieldnames=keys)
#     # 写入表头内容
#     writer.writeheader()
#     writer.writerows(rows1)
#     # for dict in rows1:
#     #     writer.writerow(dict)

# csv 对字典数据的读取
with open("test3.csv", "r", encoding='utf-8')as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(type(row))
        print(row['name'],row['age'],row['sex'])












