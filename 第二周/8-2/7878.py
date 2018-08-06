"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:7878.PY
@ide:PyCharm
@time:2018-08-02 16:43:54
"""
# 功能：具有增删改查功能的学员信息管理系统
# 选项：	  1.添加学员姓名
# 	  2.修改学员姓名
# 	  3.查询学员姓名
# 	  4.删除学员姓名
#     0.退出程序
#     添加学员：
# 		输入要添加的姓名
# 		进行添加操作
# 	修改学员：
# 		输入学员的序号
# 		输入修改信息
# 		执行修改
# 	查询学员：
# 		1.输入查询序号
# 			输入学员序号
# 			输出学员信息
# 		2.查询所有学员
# 			迭代列表，输出所有学员
# 	删除学员：
# 		1.输入序号删除
# 		2.输入学员名称删除
# 		3.删除所有学员
import sqlite3
def sqlite_into():
    create_table = "create table if NOT exists student_2(id INTEGER PRIMARY KEY ,name TEXT, age INTEGER, score FLOAT)"
    cursor.execute(create_table)

def student_into(is_choose):
    if is_choose==True:
        table_count_sql = "select count(*) from student_2"
        res = cursor.execute(table_count_sql)
        count = res.fetchone()[0]
        return count
    else:
        list_id = []
        student_select_sql = "select * from student_2"
        result = cursor.execute(student_select_sql)
        for id,name,age,score in result:
            print(id,'.',name,age,score)
            list_id.append(id)
        return list_id
# def student_count():
#     student_select_sql = "select * from student_2"
#     result = cursor.execute(student_select_sql)
#     for id, name, age, score in result:
#         print(id, '.', name, age, score)
#         list1 = list.append(str(id))
#     return list1


def insert_student():
    name = input('请输入要添加的姓名')
    age = int(input('请输入要添加的年龄：'))
    score = float(input('请输入成绩：'))
    insert_student_sql = "insert into student_2(name,age,score)VALUES ('%s',%d,%f)"%(name,age,score)
    cursor.execute(insert_student_sql)

def update_student():
    student_number = int(input('请输入你要修改学员的序号'))
    while student_number<1 or student_number>student_into(True):
        student_number = int(input('输入错误，请重新输入'))
    new_name = input('请输入要修改的姓名：')
    new_age = int(input('请输入要修改的年龄：'))
    new_score = float(input('输入要添加的分数：'))
    update_student_sql = "update student_2 set name='%s',age=%d,score=%.1f WHERE id=%d"%(new_name,new_age,new_score,student_number)
    cursor.execute(update_student_sql)

def delete_student():
    print('1-输入序号删除')
    print('2-删除所有学员')
    choose_number = int(input('请输入你选择的功能：'))
    while choose_number!=1 and choose_number!=2:
        choose_number = int(input('输入错误，请重新选择：'))
    if choose_number == 1:
        student_into(False)
        student_number = int(input('输入你要删除学员信息的序号'))

        list_id = student_into(False)
        if student_number not in list_id:
            student_number = int(input('选择错误，请重新输入：'))
        delete_student_sql = "delete from student_2 WHERE id=%d"%student_number
    if choose_number==2:
        delete_student_sql = "delete from student_2"
    cursor.execute(delete_student_sql)

if __name__ == '__main__':
    while True:
        print('''
        1-添加学员姓名
        2-修改学员姓名
        3-查询学员姓名
        4-删除学员姓名
        0-退出程序''')
        connect = sqlite3.connect('student_2.db')
        cursor = connect.cursor()
        sqlite_into()
        choose_number = int(input('输入你选择的功能：'))
        while choose_number<0 or choose_number>4:
            choose_number = int(input('输入错误，重新输入：'))
        if choose_number==1:
            insert_student()
        elif choose_number==2:
            if student_into(True)==0:
                print('信息为空')
            else:
                update_student()
        elif choose_number==3:
            if student_into(True)==0:
                print('信息为空')
            else:
                student_into(False)
        elif choose_number==4:
            delete_student()
        else:
            break
        connect.commit()
        cursor.close()
        connect.close()













