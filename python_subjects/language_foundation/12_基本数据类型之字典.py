# -*- coding:utf8 -*-
"""
@author:natural
@file:12_基本数据类型之字典.py
@time:2022/01/19
"""
# 字典 键-值（key-value）存储，具有极快的查找速度 字典就相当于 JAVA 中的 map
# 键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的。

# 创建字典
dict = {'key1': 'value1', 'key2': 'value2'}

# 访问字典 通过键找值
print(dict['key1'])

# 典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
print(dict1)
# 新增一个键值对
dict1['jack']='444444'
print(dict1)
# 修改键值对
dict1['liangdianshui']='555555'
print(dict1)

# 通过 del 可以删除 dict （字典）中的某个元素，也能删除 dict （字典）
# 通过调用 clear() 方法可以清除字典中的所有元素
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
print(dict1)
# 通过 key 值，删除对应的元素
del dict1['twowater']
print(dict1)
# 删除字典中的所有元素
dict1.clear()
print(dict1)
# 删除字典
del dict1


# len(dict)	计算字典元素个数
# str(dict)	输出字典可打印的字符串表示
# type(variable)	返回输入的变量类型，如果变量是字典就返回字典类型
# dict.clear()	删除字典内所有元素
# dict.copy()	返回一个字典的浅复制
# dict.values()	以列表返回字典中的所有值
# popitem()	随机返回并删除字典中的一对键和值
# dict.items()	以列表返回可遍历的(键, 值) 元组数组


























