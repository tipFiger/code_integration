# -*- coding:utf8 -*-
"""
@author:natural
@file:22_列表生成式与生成器.py
@time:2022/01/22
"""
# 列表生成式range
list1 = list(range(10))
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 需求: [1,4,9,16,25,36,49]
list2 = []
for i in range(1, 10):
    list2.append(i ** 2)
print(list2)

# 简化上面的代码
# 1.首先遍历(1,10)for i in range(1,10)
# 2.将遍历到的每个值,进行求平方操作 i**2
# 3.将平方后的每个值,加入列表中 []
list3 = [i ** 2 for i in range(1, 10)]
print(list3)

# 遍历之后,还可以进行if判断
list4 = [i ** 2 for i in range(1, 10) if i % 2]
print(list4)

list5 = [i ** 2 for i in range(1, 10) if not i % 2]
print(list5)

# 双重循环嵌套
list6 = [char + char2 for char in "abc" for char2 in "xyz"]
print(list6)

# for in 字典 做列表生成式
dict1 = {"name": "xiaoming", "age": "18"}
list6 = [key + "=" + value for key, value in dict1.items()]
print(list6)

# 只要支持for in都可以使用列表生成式
# [for i in list]
# [for i in tuple]
# [for i in dict]
# [for i in str]
# [for i in range()]
# [for i in set]

# 例: 将所有字符串转小写
list7 = ["Hello", "GOOD", "AABC", "kkH"]
list8 = [item.lower() for item in list7]
print(list8)

# 生成器

# 方式一：（），将列表生成式中的[]改成()
# 列表生成式的类型是list，生成器的类型是generator【当做一种新的数据类型】
r1 = (x ** 2 for x in range(1, 6))
print(r1)  # (1,4,9,16,25)
print(type(r1))

"""
for i in r1:
    print(i)
"""

# 生成器区别于列表生成式：可以使用next遍历，每调用一次则获取一个元素
# next()
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))


# 注意：当生成器中的元素全部获取完成之后，接着调用next函数的，则会出现StopIteration
# print(next(r1))   #StopIteration异常


# 方式二：yield---->让步
# (x for x in range(1,6))----->1,2,3,4,5
def test(n):
    for i in range(1, n + 1):
        # 执行到yield的时候，则函数会停止，将yiled后面的变量返回
        yield i ** 2
        # yield后面的代码的执行时机：当调用next函数的时候
        print(i)


t = test(5)
print(t)  # <generator object test at 0x0000019CC432A1A8>
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
