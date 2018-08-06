"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用函数+数据库完成学生信息管理系统.PY
@ide:PyCharm
@time:2018-08-02 14:33:37
"""
import sqlite3
# 定义一个创建表的函数
def create_table():
    # UNIQUE:表示字段的值是惟一的
    # NOT NULL：表示字段值不允许为空
    # IF NOT EXISTS：当表不存在时，在执行创建表的sql语句，如果表已经存在，则sql语句不再执行，可以避免异常。
    create_sql = "create table if not exists student(id INTEGER PRIMARY KEY UNIQUE,name TEXT,age INTEGER, score FLOAT)"
    cursor.execute(create_sql)
# 定义一个添加学员的函数
def add_student():
    name = input('请输入姓名：')
    age = int(input('请输入年龄：'))
    score = float(input('请输入分数：'))
    insert_sql = "insert into student(name,age,score)VALUES('%s', %d, %.1f)"%(name, age, score)
    cursor.execute(insert_sql)

# 定义一个查询学员信息的函数
def select_student_info(is_total_number):
    # 如果 is_total_number==True就查询表中的数据总量
    if is_total_number == True:
        # 查询表中的数据总量
        select_sql = 'select count(*) from student'
        res = cursor.execute(select_sql)
        count = res.fetchone()[0]
        return count
    # 如果 is_total_number==FAlse就查询表中的数据的详细信息
    elif is_total_number == False:
        list_id=[]
        select_sql= 'select * from student'
        result_list = cursor.execute(select_sql)
        for id,name,age,score in result_list:
            print(id,'.',name,age,score)
            list_id.append(id)
        return list_id

# 定义一个修改学员信息的函数
def update_student_info():
    # 修改之前先把所有的学员信息先查询出来
    select_student_info(False)
    select_number = int(input('请输入要修改的学员的编号：'))
    while select_number<1 or select_number>select_student_info(True):
        select_number = int(input('输入的学员编号错误，请重新输入：'))
    # 知道了要修改学员的编号，然后进行修改
    new_name = input('请输入修改后的姓名：')
    new_age = int(input('请输入修改后的年龄：'))
    new_score = float(input('请输入新的分数：'))
    update_sql = "update student set name='%s',age=%d,score=%.1f where id=%d"%(new_name,new_age,new_score,select_number)
    cursor.execute(update_sql)

# 定义一个删除学员信息的函数
def delete_student_info():
    print('1-删除指定学员的信息')
    print('2-删除所有学员信息')
    select_number = int(input('请输入要操作的编号：'))
    while select_number!=1 and select_number!=2:
        select_number = int(input('请重新输入你要操作的序号:'))
    # 如果用户选择的是1，说明用户想要删除指定的学员信息
    if select_number == 1:
        list_id = select_student_info(False)
        number = int(input('请输入要删除的学员编号：'))
        while number not in list_id:
            number = int(input('学员编号输入错误，请重新输入要删除的学员编号：'))
        delete_sql="delete from student where id=%d"%number
    else:
        delete_sql = 'delete from student'
    cursor.execute(delete_sql)

if __name__ == '__main__':
    while True:
        print('''
        1-添加学员信息
        2-修改学员信息
        3-查询学员信息
        4-删除学员信息
        0-退出程序''')
        connect = sqlite3.connect('student_def.db')
        cursor = connect.cursor()
        create_table()
        select_number = int(input('请输入要操作的序号：'))
        if select_number==1:
            add_student()
        elif select_number==2:
            while select_student_info(True)==0:
                print('修改的学员信息为空')
            else:
                update_student_info()
        elif select_number==3:
            while select_student_info(True)==0:
                print('查询的学员信息为空')
            else:
                select_student_info(False)
        elif select_number==4:
            delete_student_info()
        else:
            break
        connect.commit()
        cursor.close()
        connect.close()

