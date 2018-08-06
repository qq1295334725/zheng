"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用map函数实现把大写转换成小写字母.PY
@ide:PyCharm
@time:2018-07-27 09:55:14
"""
# 将字符串全部转换成小写字母
def char_lower(string):
    all_char_dict={'A':'a', 'B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z',}
    # 声明一个变量，记录最终的转换结果
    result = ''
    # 遍历一下string这个字符串，将其中大写字母转换成小写字母
    for char_str in string:
        if char_str.isupper():
          # 如果从string字符串中取出来的字母是大写，则从字典中取出对应的小写字母
            every_char_result = all_char_dict[char_str]
        else:
            every_char_result = char_str
        result+=every_char_result
    return result
res = char_lower('AcdbDef')
print(res)

res1 = list(map(char_lower, ['WQsfGas', 'GASgFEgds']))
print(res1)

# 整体封装
def custom_lower(a):
    def char_lower(string):
        all_char_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i','J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r','S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', }
        # 声明一个变量，记录最终的转换结果
        result = ''
        # 遍历一下string这个字符串，将其中大写字母转换成小写字母
        for char_str in string:
            if char_str.isupper():
                # 如果从string字符串中取出来的字母是大写，则从字典中取出对应的小写字母
                every_char_result = all_char_dict[char_str]
            else:
                every_char_result = char_str
            result += every_char_result
        return result
    if isinstance(a,list):
        # isinstance():判断某一个变量是否属于某一个类型，如果是返回True，如果不是返回False
        return list(map(char_lower,a))
    else:
        return char_lower(a)
res2 = custom_lower('GASjkfdGFE')
print(res2)



