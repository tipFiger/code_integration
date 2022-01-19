# -*- coding:utf8 -*-
"""
@author:natural
@file:13_基本数据类型之集合.py
@time:2022/01/19
"""

# 创建一个 set，需要提供一个 list 作为输入集合
set1 = set([123, 456, 789])
print(set1)

# 添加元素 add(key) 方法可以添加元素到 set 中，可以重复添加，但不会有效果
set1 = set([123, 456, 789])
print(set1)
set1.add(100)
print(set1)
set1.add(100)
print(set1)

# 删除元素  remove(key) 方法可以删除 set 中的元素
set1 = set([123, 456, 789])
print(set1)
set1.remove(456)
print(set1)

# set 是一个无序不重复元素集，因此，两个 set 可以做数学意义上的 union(并集), intersection(交集), difference(差集) 等操作。
set1 = set('hello')
set2 = set(['p', 'y', 'y', 'h', 'o', 'n'])
print(set1)
print(set2)

# 交集 (求两个 set 集合中相同的元素)
set3 = set1 & set2
print('\n交集 set3:')
print(set3)
# 并集 （合并两个 set 集合的元素并去除重复的值）
set4 = set1 | set2
print('\n并集 set4:')
print(set4)
# 差集
set5 = set1 - set2
set6 = set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print(set6)

# 去除海量列表里重复元素，用 hash 来解决也行，只不过感觉在性能上不是很高，用 set 解决还是很不错的
list1 = [111, 222, 333, 444, 111, 222, 333, 444, 555, 666]
set7 = set(list1)
print('\n去除列表里重复元素 set7:')
print(set7)

