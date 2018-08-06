"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:手机销售系统作业.PY
@ide:PyCharm
@time:2018-07-24 09:03:11
"""
'''
手机销售系统

	手机品牌	手机价格	库存数量
	 vivoX9		   2798		  25
	 iphone7(32G)	   4888		  31
	 iphone7(128G)	   5668		  22
	 iphone7P(128G)	   6616		  29
	 iphone6(16G)	   3858		  14
	 ....
	 ....
	 ....
phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'}, 
{'name':'iphone6s', 'price':'2200', 'count':'120'}, 
{'name':'iphone7', 'price':'4000', 'count':'80'}, 
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]
功能要求：
	四个选项：
		1.查看所有手机品牌
			1.vivoX9
			2.iphone7(32G)
			......
		        分支选项：
				1.选择产品序号查看详情(根据序号输出产品名称，价格，库存)
					1.购买(库存数量-1，库存为0时，删除该产品)
					2.返回
				2.返回
		2.更改产品库存信息
			1.添加新产品(添加新产品,包括产品名称、价格、库存)
			2.修改原有产品
			  输出所有产品信息
			  1.根据选择序号进行修改
			  2.返回
		3.移除产品库存信息
			1.查看所有产品，根据序号移除
			2.移除所有产品
			3.返回
		4.退出程序
'''
phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]
# 查看所有品牌的函数
# 设置一个形象is_detail，如果is_detail的值是True，查询手机详细信息，如果值为False，查询简要信息。
def select_all_phone(is_detail):
    for x in  range(0, len(phone_info)):
        # 取出每一个字典
        phone_dict = phone_info[x]
        # is_detali是True，即查询详细信息。
        if is_detail == True:
            print('{0}.品牌{1},价格{2},库存{3}'.format(x+1, phone_dict['name'], phone_dict['price'], phone_dict['count']))
        # 如果is_detail不是True，那就是False，查询简要信息（手机品牌）。
        else:
            print('{0}.品牌{1}'.format(x+1, phone_dict['name']))


# 定义查看某个品牌的详细信息或者返回的一个函数
def detail_info_or_back():
    print('1-根据产品序号查看手机详细信息')
    print('2-返回')
    # 根据控制台的输入数字，来进行判断运行哪个选项
    select_operation = int(input('请输入您要操作的序号：'))
    # 循环检测用户输入的序号是否符合要求
    while select_operation!=1 and select_operation!=2:
        select_operation = int(input('输入错误，请重新输入你要操作的序号：'))
    if select_operation == 1:
        select_all_phone(False)
        select_number = int(input('请输入要查询的手机详细信息手机品牌序号：'))
        while select_number<1 or select_number>len(phone_info):
            select_number = int(input('输入的序号有误，请重新输入要查询的手机详细信息的手机品牌序号：'))
        phone_dict = phone_info[select_number-1]
        print('{0}:品牌{1},价格{2},库存{3}'.format(select_number,phone_dict['name'], phone_dict['price'], phone_dict['count']))

        # 函数里面嵌套函数，因为用户选择序号1的时候，下面还有购买和返回的操作，把购买和返回的操作单独封装，最后当用户选择1的时候，之间在序号1的时候，调用buy_or_back()函数
        buy_or_back(phone_dict)
    # 如果选择的不是序号1，那么就是序号2，返回
    else:
        return

# 定义一个购买或者返回的函数,设置一个参数接收某手机的字典信息
def buy_or_back(phone_dict):
    print('1-购买')
    print('2-返回')
    select_number = int(input('请选择要操作的编号：'))
    while select_number !=1 and select_number !=2:
        select_number = int(input('输入错误，请重新选择要操作的序号：'))
    # 选择序号一，说明用户要购买手机
    if select_number == 1:
        # 在输入购买数量之前，先提示手机有多少库存
        total_count = int(phone_dict['count'])
        print('当前库存%s台'%total_count)
        # 当用户知道库存数量之后，让用户输入要购买的数量。
        buy_count = int(input('请输入要购买的数量：'))
        while buy_count<=0 or buy_count>total_count:
            buy_count = int(input('输入错误，请重新输入要购买的数量：'))
        # 根据购买的数量，计算剩余库存，修改原有的库存数量
        surplus_count = total_count - buy_count
        # 将剩余的库存存入到原有的字典中
        phone_dict['count'] = str(surplus_count)
        # 假如用户给手机全部买完，库存为0，将该手机品牌从该列表中移除
        if int(phone_dict['count']) == 0:
            phone_info.remove(phone_dict)
        print('购买成功！')
    # 选择的序号2 ，返回
    else:
        return

# 定义一个添加产品或修改产品的函数
def add_or_update_info():
    print('1-添加新产品')
    print('2-修改原有产品')
    select_number = int(input('请输入要选择的序号：'))
    while select_number!=1 and select_number!=2:
        select_number = int(input('输入错误！请重新输入：'))
    if select_number == 1:#如果选择序号1，则添加新产品
        new_phone_name = input('请输入新产品名称：')
        new_phone_price = input('请输入新产品价格：')
        new_phone_count = input('请输入新产品库存：')
        # 将新产品的名称，价格，库存存入新的字典中
        new_phone_dict = {'name':new_phone_name,'price':new_phone_price ,'count':new_phone_count}
        # 将新的字典添加到列表中
        phone_info.append(new_phone_dict)
        print('新产品添加成功！')
    # 选择2，则修改原有产品
    else:
        # 调用select_all_phone函数，参数设置为True，将所有的手机详细信息全部打印出来，用户再根据对应的编号修改选择要修改那个手机信息
        select_all_phone(True)
        print('1-根据序号修改产品信息')
        print('2-返回')
        select_number = int(input('请输入你要操作的序号：'))
        while select_number!=1 and select_number!=2:
            select_number = int(input('输入错误！请重新输入你要操作的序号：'))
        # 如果选择的序号1，则根据产品序号修改产品信息
        if select_number == 1:
            phone_num = int(input('请输入要修改的手机序号：'))
            while phone_num<1 or phone_num>len(phone_info):
                phone_num = int(input('手机序号输入错误！请重新输入要修改的手机序号：'))
            update_dict = phone_info[phone_num - 1]
            update_name = input('请输入修改的名称：')
            update_price = input('请输入修改的价格：')
            update_count = input('请输入修改的库存：')
            update_dict['name'] = update_name
            update_dict['price'] = update_price
            update_dict['count'] = update_count
            print('修改成功！')
        else:
            return

# 定义一个删除产品或者返回的函数
def delete_phone_or_back():
    print('1-根据产品序号删除产品')
    print('2-删除所有产品')
    print('3-返回')
    select_number = int(input('请输入要操作的序号：'))
    while select_number!=1 and select_number!=2:
        select_number = int(input('输入错误！请重新选择：'))
    # 用户选择1，根据产品序号删除
    if select_number == 1:
        select_all_phone(True)
        number = int(input('请输入要删除的产品序号：'))
        while number<1 or number>len(phone_info):
            number = int(input('输入错误！请重新选择要删除的产品编号：'))
        del phone_info[number - 1]
    elif select_number == 2:#用户选择2 ，全部删除
        while len(phone_info):
            del phone_info[0]
    elif select_number == 3:#用户选择3，返回
        return

while True:
    print('''
    欢迎使用手机操作系统
    1-查看所有手机品牌
    2-添加或修改手机信息
    3-删除手机信息
    4-退出程序''')
    select_number = int(input('请输入要操作的序号：'))
    while select_number<=0 or select_number>4:
        select_number = int(input('输入错误！请重新选择：'))
    if select_number == 1:
        if len(phone_info):
            detail_info_or_back()
        else:
            print('没有手机信息，程序结束！')
            break
    elif select_number == 2:
        add_or_update_info()
    elif select_number == 3:
        delete_phone_or_back()
    elif select_number == 4:
        break
















