# -*- coding:utf8 -*-
"""
@author:natural
@file:15_循环语句.py
@time:2022/01/19
"""
# for循环
for letter in 'Hello':
    print(letter)
# 嵌套for循环
for i in 'Hello':
    for j in 'world':
        print(j)
    print(i)
# for else
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 是一个合数' % num)
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)

# rang() 生成左闭右开的整数序列。 与for循环搭配使用
for i in range(3):
    print(i)

# while循环
count = 5
while count <= 10:
    # print(count)
    count += 1
    print(count)
# 循环带条件
count = 1
sum = 0
while count <= 100:
    sum += count
    if sum > 1000:  # 当 sum 大于 1000 的时候退出循环
        break
    count = count + 1
print(sum)
# for 循环主要用在迭代可迭代对象的情况。
# while 循环主要用在需要满足一定条件为真，反复执行的情况。 （死循环+break 退出等情况。）
# 部分情况下，for 循环和 while 循环可以互换使用。
