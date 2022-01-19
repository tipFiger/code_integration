# -*- coding:utf8 -*-
"""
@author:natural
@file:9_基本数据类型之类型转换.py
@time:2022/01/19
"""
# 整型 只保留整数位
from setuptools._vendor.pyparsing import unichr

print(int(0.1))
print(int(0.5))
# 浮点型
print(float(5))
# 创建一个复数
print(complex(5))
# 对象转字符串
int1 = str(100)
print(int1)
print(type(int1))
# 对象转为表达式字符串
print(repr(10))
# 用来计算在字符串中的有效 Python 表达式,并返回一个对象 入参是字符串
o = eval('100')
print(type(o))
# 将序列 s 转换为一个元组
print(type(tuple([1, 2])))
# 将序列 s 转换为一个列表
print(type(list((1, 2))))
# 将一个整数转换为一个字符
print(type(chr(9)))
# 将一个整数转换为 Unicode 字符  需要导包才能用
print(str(unichr(9)))
# ord 将一个字符转换为它的整数值 ASCCI码的转换
print(ord('A'))
# 将一个整数转换为一个十六进制字符串
print(hex(10))
# 将一个整数转换为一个八进制字符串
print(oct(1))



















