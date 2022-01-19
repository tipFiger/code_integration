# -*- coding:utf8 -*-
"""
@author:natural
@file:10_基本数据类型之列表.py
@time:2022/01/19
"""
# 列表：List （列表）是 Python 内置的一种数据类型。 它是一种有序的集合，可以随时添加和删除其中的元素。

# 创建列表:列表就是用中括号 [] 括起来的数据，里面的每一个数据就叫做元素。每个元素之间使用逗号分隔
list1 = ['两点水', 'twowter', 'liangdianshui', 123]
print(list1)

# 访问列表的值 索引访问   0开始 所以2是第三个
print(list1[2])
# 通过方括号的形式来截取列表中的数据  不取最后一个数  所以取得是 0 1  左闭右开区间
print(list1[0:2])

# 更新列表元素
# 通过索引对列表的数据项进行修改或更新
list1[1] = '2点水'
print(list1)

# 添加列表元素使用 append() 方法来添加列表项
list1.append('六点水')
print(list1)

# 删除列表元素
del list1[3]
print(list1)

# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表
l1 = [1]
l2 = [2]
print(l1 + l2)
print(l1 * 2)

# 函数&方法	描述
# len(list)	列表元素个数
# max(list)	返回列表元素最大值
# min(list)	返回列表元素最小值
# list(seq)	将元组转换为列表
# list.append(obj)	在列表末尾添加新的对象
# list.count(obj)	统计某个元素在列表中出现的次数
# list.extend(seq)	在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)	从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)	将对象插入列表
# list.pop(obj=list[-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)	移除列表中的一个元素（参数是列表中元素），并且不返回任何值
# list.reverse()	反向列表中元素
# list.sort([func])	对原列表进行排序














