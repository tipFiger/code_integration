# -*- coding:utf8 -*-
"""
@author:natural
@file:25_递归.py
@time:2022/01/22
"""


# 递归就是在函数内部调用自己的函数被称之为递归

# 将 10不断除以2，直至商为0，输出这个过程中每次得到的商的值。
def recursion(n):
    v = n // 2  # 地板除，保留整数
    print(v)  # 每次求商，输出商的值
    if v == 0:
        ''' 当商为0时，停止，返回Done'''
        return 'Done'
    v = recursion(v)  # 递归调用，函数内自己调用自己


recursion(10)  # 函数调用


# 1、必须有一个明确的结束条件
# 2、每次进入更深一层递归时，问题规模(计算量)相比上次递归都应有所减少
# 3、递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）

# 递推：像上边递归实现所拆解，递归每一次都是基于上一次进行下一次的执行，这叫递推
# 回溯：则是在遇到终止条件，则从最后往回返一级一级的把值返回来，这叫回溯

# 递归求阶乘：1！+2！+3！+4！+5！+...+n!
def factorial(n):
    ''' n表示要求的数的阶乘 '''
    if n == 1:
        return n  # 阶乘为1的时候，结果为1,返回结果并退出
    n = n * factorial(n - 1)  # n! = n*(n-1)!
    return n  # 返回结果并退出


res = factorial(5)  # 调用函数，并将返回的结果赋给res
print(res)  # 打印结果


# 递归推斐波那契数列：# 1，1，2，3，5，8，13，21，34，55，试判断数列第十五个数是哪个？
def fabonacci(n):
    ''' n为斐波那契数列 '''
    if n <= 2:
        ''' 数列前两个数都是1 '''
        v = 1
        return v  # 返回结果，并结束函数
    v = fabonacci(n - 1) + fabonacci(n - 2)  # 由数据的规律可知，第三个数的结果都是前两个数之和，所以进行递归叠加
    return v  # 返回结果，并结束函数


print(fabonacci(15))  # 610    调用函数并打印结果

# 二分法找有序列表指定值
data = [1, 3, 6, 13, 56, 123, 345, 1024, 3223, 6688]


def dichotomy(min, max, d, n):
    '''
    min表示有序列表头部索引
    max表示有序列表尾部索引
    d表示有序列表
    n表示需要寻找的元素
    '''
    mid = (min + max) // 2
    if mid == 0:
        return 'None'
    elif d[mid] < n:
        print('向右侧找！')
        return dichotomy(mid, max, d, n)
    elif d[mid] > n:
        print('向左侧找！')
        return dichotomy(min, mid, d, n)
    else:
        print('找到了%s' % d[mid])
        return


res = dichotomy(0, len(data), data, 222)
print(res)





