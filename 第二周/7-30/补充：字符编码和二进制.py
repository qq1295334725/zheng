"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:补充：字符编码和二进制.PY
@ide:PyCharm
@time:2018-07-30 09:04:28
"""
# ---------------------二进制----------------------
# 计算机中存储的信息都是二进制的，因为计算机底层只能识别二进制0和1，我们存进计算机的所有信息都最终会转换成二进制的0和1，供计算机识别。

# -------------ASCII--------------------------
# 为了让计算机识别英文，将英文字母给予一些固定的编号，然后将这些编号转换成二进制，那么计算机就能准确 的识别这些英文字母，于是便产生了ASCII码。ASCII码使用了指定的7位或8位二进制数字的组合来表示256中可能的字符，但是实际上ASCII码表中只有128个ASCII码，剩余128字符留作扩展。

# ------------GB2312/GBK/GB18030--------------------
# 由于计算机是美国人发明的，美国人解决了让英文字母被计算机识别的难度，但是中文如何让计算机识别？于是，国家标准局于1980年颁布了GB2312编码，使计算机可以识别7000多个字符。1995年颁布了GBK1.0（21003个汉字），计算机可以识别2万多个汉字，2000年颁布了GB18030，使计算机可以识别27000多个汉字。

# ---------Unicode-----------------------
# 英文和中文已经能被计算机识别，但是全球有很多很多的国家，不可能一个国家对应一种编码，为了让计算机能够识别各个国家的语言。于是便出现了Unicode编码（统一码，万国码），这样每个国家都可以使用Unicode编码来最终实现被计算机所识别。

# ------------utf-8--------------------
# 由于Unicode会占用过多的存储空间，所以出现了utf-8编码，utf-8实现了对Unicode编码的压缩和优化，它只是Unicode的一种实现方式。

# Python2中默认使用的是ASCII码，所以使用Python2 中写代码的时候，如果代码中包含中文，将会报错，因为默认使用的ASCII码不能识别中文，所以在python2中每个.py文件的开头位置都会声明一个编码格式为coding：utf-8，这样计算机就能识别python2代码中写的中文。


# python3中默认使用的就是utf-8编码，它可以对中文字符进行编码和解码，所以即使不在文件的开头位置指定字符编码文件也能正常运行，但是为了防止出现问题，或者为了兼容python2和python3，最好在文件开头位置声明编码格式coding：utf-8。


# 编码encode
# 解码decode










