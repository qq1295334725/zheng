"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:sqlite3的基本用法.PY
@ide:PyCharm
@time:2018-08-02 09:10:27
"""
# 什么是数据库？数据库是用于保存大量的格式统一的数据，比如name，age，sex，score，数据库的内部结构是由多个表table构成的，每一个表中由很多的字段组成。
# 数据库管理多张表，表管理多个字段，字段里面存着数据。

# 数据库的分类：关系型数据库和非关系型数据库。

# ---------------------关系型数据库--------------
# 关系型数据库的特点：表和字段，数据和数据之间都存在着联系。
# 优点：1.数据之间都存在着相互的联系，有利于数据之间的增删改查
# 2.关系型数据库有事务操作，能保证数据的完整性和一致性。

# 缺点：1.数据和数据之间存在着关系，它的底层运行了大量的算法，这样会降低系统的效率和性能。
# 2.面对海量数据的增删改查和数据的维护会显得无能为力。

# 常见的关系型数据库：sqlite3,MySQL,Oracle,SQLServer

# --------------------非关系型数据库-----------
# 非关系型数据库：数据和数据之间不存在着联系，他们之间是单独存在的
# 优点：1.可以对海量的数据进行增删改查
# 2.对海量的数据进行维护和处理的效率高

# 缺点：1.非关系型数据库数据和表之间没有关系，所以也没有强大的事务关系，更没有办法保证数据的完整性和安全性。
# 2.虽然处理海量的数据库效率很高，但是安全性很差。

# 常见的非关系型数据库：redis,MongoDB


# sqlite3是python内置的一种轻量级的数据库。
import sqlite3

# 数据库的操作的三个步骤：
# 1.先连接数据库文件
# 2.进行数据库的写入和读取
# 3.关闭数据库

# 1.connect()：负责数据库连接的一个函数，当要连接的数据库文件不存在的时候，会默认在当前目录下自动创建一个新的数据库文件。
connect = sqlite3.connect('database.db')
# 2.要操作数据库，先要获取数据库游标，通过游标来操作数据库，接着对表进行增删改查。
cursor = connect.cursor()
# 3.数据库文件连接好了，游标也创建好了，接着就可以创建表，并且对表里的数据进行增删改查。
# 创建表
# student表名
# id,name,age,score:表的字段
# INTEGER,TEXT,FLOAT:数据类型
# PRIMARY KEY:给id这个字段添加约束，将id这个字段作为主键。
# 主键：主键是唯一的，不允许重复的，主要是给某一条数据设置一个唯一的，方便数据的查找和定位。
creat_table = "create table student(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,score FLOAT)"
# 通过游标执行创建表的sql语句
# cursor.execute(creat_table)

# 向表中插入一条数据（sql语句）
insert_sql = "insert into student(name,age,score)VALUES('李四', 20, 98.8)"
# cursor.execute(insert_sql)

# 更改表中的数据（sql语句）
# where:后面跟的是筛选条件
update_sql = "update student set name='%s',age=%d,score=%.1f WHERE id=2"%('张三',29,78)
# cursor.execute(update_sql)

# 查询表中的数据
# *查询表中所有的数据
select_sql = "select * from student"
# result = cursor.execute(select_sql)
# print(result)
# fetchone()：获取结果集的一条数据，返回的是一个由字段对应的数据组成的一个元组。
# print(result.fetchone())
# print(result.fetchone())
# fetchall():获取结果集中的所有数据，一条数据对应一个元组，然后再将这些元组嵌套在列表中进行返回
# print(result.fetchall())
# res = result.fetchall()
# for tuple_test in res:
#     print('id是%s'%tuple_test[0])
#     print('name是%s' % tuple_test[1])
#     print('age是%s' % tuple_test[2])
#     print('score是%s' % tuple_test[3])

# for x in result:
#     print(x)


# 删除表中的数据（sql语句）
delete_sql = "delete from student WHERE id=1"
cursor.execute(delete_sql)


# 执行提交的操作
connect.commit()
# 关闭游标
cursor.close()
# 关闭数据库
connect.close()

# 小练习：
# 1.创建一个数据库teacher
# 2.创建一个表tea，字段（id(主键)，name，age，sex）
# 3.往tea表中插入数据（张三，20，男）
# 4.往tea表中插入数据（李四，30，女）
# 5.修改（李四，30，女）这条数据，改为（王五，22，男）
# 6.删除（张三，男，20）这条数据
# 7.将表中所有的数据查询出来

# 1.创建新表
# create table tabname(col1 type1 [not null] [primary key],col2 type2 [not null],..)
# 2.删除表
# drop table tabname
# 3.查询：select * from table1 where 范围
# 4.插入：insert into 表名(字段名1,字段名2) values(值1,值2)
# 5.删除：delete from table1 where 范围
# 6.修改：update 表名 set 修改的字段名=修改的字段值 where 范围
# 7.查找：select * from table1 where 字段名 like ’%value1%’ N%匹配以N开头     %N匹配以N结尾   %N%匹配包含N
# 	[a,b]% 以a或b开头     %[a,b]以a或b结尾
# 	select * from table1 where field1 like 'z_'以z开头且匹配之后一个字符
# 	升序输出数据记录
# 	select * from table_name order by field asc
# 	降序输出数据记录
# 	select * from table_name order by field desc
# 9.总数：select count (*) from table_name;






