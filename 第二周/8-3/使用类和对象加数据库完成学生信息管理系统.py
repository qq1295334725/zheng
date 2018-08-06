"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用类和对象加数据库完成学生信息管理系统.PY
@ide:PyCharm
@time:2018-08-03 14:09:12
"""
import sqlite3
# 声明一个数据模型类：只包含属性，不包含操作属性的函数
class StudentModle(object):
    def __init__(self,db_name,table_name,field_name,field_age,field_score,field_id):
        self.db_name = db_name
        self.table_name = table_name
        self.field_name = field_name
        self.field_age = field_age
        self.field_score = field_score
        self.field_id = field_id
# 声明一个工具类，工具类一般只包含操作函数，不包含属性
class DBManager(object):
    # 定义一个创建库和游标的函数
    # stu_obj:StudentModle类生成的对象
    # stu_obj.db_name:StudentModle类中的db_name属性，对应的就是数据库名称
    def create_connet_and_cursor(self,stu_obj):
        self.connet = sqlite3.connect(stu_obj.db_name)
        self.cursor = self.connet.cursor()

    # 定义一个创建表的函数
    def create_table(self,stu_obj):
        create_sql = "create table if not exists student"+stu_obj.table_name+"(%s INTEGER PRIMARY KEY,%s TEXT,%s TEXT,%s TEXT)"%(stu_obj.field_id,stu_obj.field_name,stu_obj.field_age,stu_obj.field_score)
        self.cursor.execute(create_sql)

    # 定义一个添加数据的函数
    def insert_student_info(self,stu_obj):
        name = input('请输入添加学员的姓名：')
        age = int(input('请输入添加学员的姓名：'))
        score = int(input('请输入添加学员的姓名：'))
        inser_sql = "insert into "+stu_obj.table_name+"(%s,%s,%s) values (%s,%s,%s)"%(stu_obj.field_name,stu_obj.field_age,stu_obj.field_score,name,age,score)
        self.cursor.execute(inser_sql)

    # 定义一个查询数据库数据总量的函数
    def get_toble_count(self,stu_obj):
        select_sql="select count(*) from %s"%(stu_obj.table_name)
        res = self.cursor.execute(select_sql)
        count= res.fetchone()[0]
        return count
    # 定义一个能否查询到ID对应数据的函数
    def get_id_true_or_false(self,stu_obj,number):
        select_number = "select * from %s where id=%d"%(stu_obj.table_name,number)
        res = self.cursor.execute(select_number)
        result = res.fetchall()
        return len(result)

    # 定义一个查询数据的函数
    def select_student_info(self,stu_obj):
        count = self.get_toble_count(stu_obj)
        if count!=0:
            select_sql = "select * from "+stu_obj.table_name
            result = self.cursor.execute(select_sql)
            for id,name,age,score in result:
                print(id,'.',name,age,score)
        else:
            print('学员信息为空，无法查询')
    # 定义一个更改数据的函数
    def update_student_info(self,stu_obj):
        count = self.get_toble_count(stu_obj)
        if count!=0:
            self.select_student_info(stu_obj)
            number = int(input('请输入要修改的学员的编号：'))
            while self.get_id_true_or_false(stu_obj,number)==False:
                number = int(input('输入错误，请重新输入要修改的学员编号：'))
            name = input('请输入新的姓名：')
            age = int(input('请输入新的年龄：'))
            score = int(input('请输入新的分数：'))
            update_sql="update"+stu_obj.table_name+"set %s='%s',%s='%s',%s='%s' where %s=%s"%(stu_obj.field_name,name,stu_obj.field_age,age,stu_obj.field_score,score,stu_obj.field_id,number)
            self.cursor.execute(update_sql)
        else:
            print('学员信息为空，无法修改')
    # 定义删除数据的函数
    def delect_test(self,stu_obj):
        count= self.get_toble_count(stu_obj)
        if count!=0:
            self.select_student_info(stu_obj)
            print('1-根据学员序号删除学员信息')
            print('2-删除所有学员信息')
            select_number = int(input('请输入你要操作的序号：'))
            while select_number!=1 and select_number!=2:
                select_number = int(input('输入错误，重新输入：'))
            if select_number==1:
                number = int(input('请输入要删除的学员序号：'))
                while self.get_id_true_or_false(stu_obj,number)==False:
                    number = int(input('序号输入错误，请重新输入要删除的学员序号：'))
                delect_sql = "delect from %s where id=%d"%(stu_obj.table_name,number)
            else:
                delect_sql = "delect from %s"%(stu_obj.table_name)
            self.cursor.execute(delect_sql)
        else:
            print('学员信息为空，无法删除')
    # 定义一个关闭数据库连接和游标的函数
    def close_db_and_commit(self):
        self.connet.commit()
        self.cursor.close()
        self.connet.close()


if __name__ == '__main__':
    student = StudentModle('Student_Plus.db','student','name','age','score','id')
    db_manager = DBManager()
    db_manager.create_connet_and_cursor(student)
    db_manager.create_table(student)
    while True:
        print('''
        1-添加学员信息
        2-修改学员信息
        3-查询学员信息
        4-删除学员信息
        0-退出程序
        ''')
        select_number=int(input('请选择操作序号：'))
        while select_number<0 or select_number>4:
            select_number = int(input('输入错误，请重新选择操作序号：'))
        if select_number==1:
            db_manager.insert_student_info(student)
        elif select_number==2:
            db_manager.update_student_info(student)
        elif select_number==3:
            db_manager.select_student_info(student)
        elif select_number==4:
            db_manager.delect_test(student)
        else:
            db_manager.close_db_and_commit()





