"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:11.PY
@ide:PyCharm
@time:2018-07-24 15:47:26
"""
phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]
# 查看手机全部信息（True），查看手机部分信息（False）
def phone_all_back(is_choose):
    for x in range(0, len(phone_info)):
        phone_dict = phone_info[x]
        if is_choose == True:
            print('{0}.品牌{1}，价格{2}，库存{3}'.format(x+1, phone_dict['name'], phone_dict['price'], phone_dict['count']))
        else:
            print('{0}.{1}'.format(x+1, phone_dict['name']))

# 查看手机品牌
def select_or_look():
    print('1-选择产品序号查看详情')
    print('2-返回')
    choose_number = int(input('请输入你要选择的功能：'))
    while choose_number!=1 and choose_number!=2:
        choose_number = int(input('输入错误！请重新输入你要选择的功能：'))
    if choose_number == 1:
        phone_all_back(False)
        phone_number = int(input('请输入你要查看手机详细信息的序号：'))
        while phone_number<1 or phone_number>len(phone_info):
            phone_number = int(input('输入错误！请重新输入你要查看手机详细信息的序号：'))
        phone_dict = phone_info[phone_number - 1]
        print('{0}.品牌{1}，价格{2}，库存{3}'.format(phone_number, phone_dict['name'], phone_dict['price'], phone_dict['count']))
        buy_or_return(phone_dict)
    else:
        return

# 购买手机
def buy_or_return(phone_dict):
    print('1-购买')
    print('2-返回')
    choose_num = int(input('请输入你选择的功能序号：'))
    while choose_num!=1 and choose_num!=2:
        choose_num = int(input('输入错误！请重新输入你要选择的功能序号：'))
    if choose_num == 1:
        surplus_phone = int(phone_dict['count'])
        print('手机库存%s台'%surplus_phone)
        buy_phone = int(input('请输入你要购买的数量：'))
        while buy_phone<1 or buy_phone>surplus_phone:
            buy_phone = int(input('输入错误！请重新输入你要购买的数量：'))
        surplus_num = surplus_phone - buy_phone
        phone_dict['count'] = surplus_num
        print('购买成功！')
        if surplus_num == 0:
            phone_info.remove(phone_dict)
    else:
        return

def change_phone():
    print('1-添加新产品')
    print('2-修改原有产品')
    choose_number = int(input('请输入你选择的功能：'))
    while choose_number!=1 and choose_number!=2:
        choose_number = int(input('输入错误！请重新输入你选择的功能：'))
    if choose_number == 1:
        update_name = input('请输入要添加的名称：')
        update_price = input('请输入要添加的价格：')
        update_count = input('请输入要添加的库存：')
        new_phone_dict = {'name':update_name, 'price':update_price, 'count':update_count}
        phone_info.append(new_phone_dict)
        print('添加成功！')
    elif choose_number == 2:
        phone_all_back(True)
        print('1-根据选择序号进行修改')
        print('2-返回')
        choose1_number = int(input('请输入你要操作的序号：'))
        while choose1_number!=1 and choose1_number!=2:
            choose1_number = int(input('输入错误！重新选择你要操作的序号'))
        if choose1_number == 1:
            choose_num = int(input('请选择你要修改产品的序号：'))
            while choose_num<1 or choose_num>len(phone_info):
                choose_num = int(input('输入错误！请重新输入你要修改产品的序号：'))
            phone_dict = phone_info[choose_num - 1]
            phone_dict['name'] = input('请输入要修改的名称：')
            phone_dict['price'] = input('请输入要修改的价格：')
            phone_dict['count'] = input('请输入要修改的库存：')
            print('修改成功！')
        else:
            return

def delect_phone():
    print('''
    1-根据序号删除
    2-移除所有产品
    3-返回''')
    choose_number = int(input('请输入你要选择的功能：'))
    while choose_number<1 or choose_number>3:
        choose_number = int(input('输入错误！请重新输入你要选择的功能：'))
    if choose_number == 1:
        phone_all_back(True)
        choose_num = int(input('请输入你要删除的序号：'))
        while choose_num<1 or choose_num>len(phone_info):
            choose_num = int(input('输入错误！请重新输入你要删除的序号：'))
        del phone_info[choose_num - 1]
        print('删除成功！')
    elif choose_number == 2:
        phone_info.clear()
        print('清除成功！')
    elif choose_number == 3:
        return

while True:
    print('''
    欢迎来到手机销售系统
    1-查看所有手机品牌
    2-更改产品库存信息
    3-移除产品库存信息
    4-退出程序''')
    choose_number = int(input('请输入你要选择的功能序号：'))
    while choose_number<1 or choose_number>4:
        choose_number = int(input('输入错误！请重新输入你要选择的序号：'))
    if choose_number == 1:
        while len(phone_info) == 0:
            print('无手机信息')
            break
        else:
            select_or_look()
    elif choose_number == 2:
        while len(phone_info) == 0:
            print('无手机信息')
            break
        else:
            change_phone()
    elif choose_number == 3:
        delect_phone()
    elif choose_number == 4:
        break




