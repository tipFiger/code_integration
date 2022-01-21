# -*- coding:utf8 -*-
"""
@author:natural
@file:20_匿名函数.py
@time:2022/01/22
"""
# lambda 来创建匿名函数
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

sum = lambda num1, num2: num1 + num2
print(sum(1, 2))

# lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的
num2 = 100
sum1 = lambda num1: num1 + num2

num2 = 10000
sum2 = lambda num1: num1 + num2

print(sum1(1))
print(sum2(1))

# 三元运算换成匿名函数
calc = lambda x, y: x * y if x > y else x / y
print(calc(2, 5))

# 列表[1,2,3,4,5,6,7,8,9],返回一个n*n 的列表
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x * x, li)))

# 接受一个list并利用reduce()求积
from functools import reduce

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reduce(lambda x, y: x * y, li))

# 在一个list中，删掉偶数，只保留奇数
li = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(lambda x: x % 2 == 1, li)))  # [1, 5, 9, 15]

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
li = list(range(1, 200))
print(list(filter(lambda x: int(str(x)) == int(str(x)[::-1]), li)))

# 对列表按照绝对值进行排序
li = [-21, -12, 5, 9, 36]
print(sorted(li, key=lambda x: abs(x)))
