# -*- coding:utf8 -*-
"""
@author:natural
@file:17_定义函数.py
@time:2022/01/21
"""


# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段

# 定义函数
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
# 函数的第一行语句可以选择性地使用文档字符串（用于存放函数说明）
# 函数内容以冒号起始，并且缩进
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None

# "两数之和"
def sum(num1, num2):
    return num1 + num2


# 调用函数
print(sum(5, 6))


# 不带参数值的 return 语句返回 None
def sum(num1, num2):
    # 两数之和
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError('参数类型错误')
    return num1 + num2


print(sum(1, 2))


# 函数也可以返回多个值
def division(num1, num2):
    # 求商与余数
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a


num1, num2 = division(9, 4)
tuple1 = division(9, 4)

print(num1, num2)
print(tuple1)  # 一次接受多个返回值的数据类型就是元组


# 默认参数 只有在形参表末尾的那些参数可以有默认参数值
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


# 调用 print_user_info 函数

print_user_info('x', 18, '女')
print_user_info('y', 25)


# 赋给形参的值是根据位置而赋值的。例如，def func(a, b=1) 是有效的，但是 def func(a=1, b) 是 无效 的
# 如果 b 是一个 list ，可以使用 None 作为默认值
def print_info(a, b=None):
    if b is None:
        b = []
    return


# 默认参数的值是不可变的对象，比如None、True、False、数字或字符串
def print_info(a, b=[]):
    print(b)
    return b


result = print_info(1)

result.append('error')

print_info(2)


# 关键字参数（位置参数） 通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


# 调用 print_user_info 函数

print_user_info(name='x', age=18, sex='女')
print_user_info(name='y', sex='女', age=18)


# 不定长参数 *args 任意形参
def print_user_info(name, age, sex='男', *hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby))
    return


# 调用 print_user_info 函数
print_user_info('x', 18, '女', '打篮球', '打羽毛球', '跑步')


# 不定长参数 **kwargs 任意关键字参数
def print_user_info(name, age, sex='男', **hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby))
    return


# 调用 print_user_info 函数
print_user_info(name='x', age=18, sex='女', hobby=('打篮球', '打羽毛球', '跑步'))


# 强制使用关键字参数传递
def print_user_info(name, *, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return;


# 调用 print_user_info 函数
print_user_info(name='c', age=18, sex='女')

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
# print_user_info( '两点水' , 18 , '女' )
print_user_info('c', age='22', sex='男')


# 字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象
def chagne_number(b):
    print('函数中一开始 b 的值：{}'.format(b))
    b = 1000
    print('函数中 b 赋值后的值：{}'.format(b))


b = 1
chagne_number(b)
print('最后输出 b 的值：{}'.format(b))


def chagne_list(b):
    print('函数中一开始 b 的值：{}'.format(b))
    b.append(1000)
    print('函数中 b 赋值后的值：{}'.format(b))


b = [1, 2, 3, 4, 5]
chagne_list(b)
print('最后输出 b 的值：{}'.format(b))








