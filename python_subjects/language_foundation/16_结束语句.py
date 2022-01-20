# -*- coding:utf8 -*-
"""
@author:natural
@file:16_结束语句.py
@time:2022/01/19
"""
# 循环控制语句： 控制语句是为了让我们告诉程序什么时候停止，什么时候不运行这次循环。
# break	在语句块执行过程中终止循环，并且跳出整个循环
# continue	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
# pass	pass 是空语句，是为了保持程序结构的完整性

# for 循环使用 break
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)

# for 循环使用 continue
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

# while中使用break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

# while中使用 continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')


# pass 不做任何事情，一般用做占位语句
def fun():
    pass
