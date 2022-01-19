# -*- coding:utf8 -*-
"""
@author:natural
@file:11_基本数据类型之元组.py
@time:2022/01/19
"""
# 元组（tuple） 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，insert() 这样的方法，
# 但它也有获取某个索引值的方法，但是不能赋值。

# 创建元组 括号中添加元素，并使用逗号隔开即可
tuple1 = ('两点水', 'twowter', 'liangdianshui', 123, 456)
tuple2 = '两点水', 'twowter', 'liangdianshui', 123, 456
print(tuple1, tuple2)
# 空元组
tuple3 = ()
# 只包含一个元素时，需要在元素后面添加逗号
print(type((1,)))

# 访问元组 元组下标索引也是从 0 开始，元组（tuple）可以使用下标索引来访问元组中的值。
print(tuple2[1])

# 元组不可变，但元组里面有列表就可变
list1 = [1,2]
t1 = (1, list1)
list1[0] = 4
print(t1)

# 删除元组：只能通过删除整个元组，来删除元素
tuple1=('两点水','twowter','liangdianshui',[123,456])
print(tuple1)
del tuple1

# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组

# 元组内置函数
# len(tuple)	计算元组元素个数
# max(tuple)	返回元组中元素最大值
# min(tuple)	返回元组中元素最小值
# tuple(seq)	将列表转换为元组













