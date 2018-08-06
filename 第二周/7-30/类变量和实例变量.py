"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:类变量和实例变量.PY
@ide:PyCharm
@time:2018-07-30 15:46:37
"""
# 类变量：所有实例化的对象都可以共享的变量，叫做类变量。类变量一般函数体之外定义。
# 实例变量：只有实例变量对象才能调用的变量，称为实例变量。对象的属性也可以称之为实例变量
class Employee(object):
    # 声明一个类变量，记录员工的总人数
    total_employee_number = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # 在 __init__函数里面调用total_employee_number这个类变量
        Employee.total_employee_number+=1

    def get_total_number(self):
        print('员工总人数：',Employee.total_employee_number)

# 类变量在各个对象之间数据是共享的，类只初始化一次。
e1 = Employee('张三',6000)
print(e1.name)
# 实例变量的调用：对象名.实例变量
e1.get_total_number()
e2 = Employee('李四', 8000)
e2.get_total_number()
print(e1.total_employee_number,'=============')
# 类变量的调用：类名.类变量
print(Employee.total_employee_number)


