# -*- coding:utf8 -*-
"""
@author:natural
@file:24_装饰器.py
@time:2022/01/22
"""


# 装饰器:  在不修改函数的情况下,为函数增加功能! (基于闭包)

def show():
    print("秀")


# 想打出"天秀",做一个闭包

# 装饰器创建步骤:
# 1.先写出标准的闭包
# 2.在外层函数中接收一个函数为形参fn
# 3.在闭包(inner)中将这个传入的函数fn调用:fn()
# 4.将新增的功能实现,实现在闭包(inner)中.
# def outer(fn):              # 对于装饰器fn必须是函数
# 	def inner():
# 		fn()
# 		print("天秀")     # 需要添加的功能
# 	return inner
#
# f = outer(show)       # 调用ouer函数,并传入show函数作为参数 show == fn
#                       # 对于装饰器,这个参数必须是函数,其他类型一律不接!
#                       # f = inner 返回的inner
#
# f()                   # inner().  调用inner时,第一步就会执行show函数,
# 第二步才是执行增加的功能

# 写一个装饰器,为show函数添加一句打印"蒂花之秀",先打印"蒂花之秀",show后打印

# def show2(X):
# 	def show3():
# 		print("蒂花之秀")
# 		X()
# 	return show3
#
# Y = show2(show)
#
# Y()

# 给一个函数添加打印9*9乘法表
def show():
    print("秀")


def outer(fn):
    def inner():
        fn()
        # 这个才是每个装饰器不同的操作
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("%d*%d=%d" % (j, i, j * i), end=" ")
            print(" ")

    return inner


f = outer(show)
f()


@outer  #
def show():
    print("秀")


show()


def getAge(age):
    print(age)


# getAge(10)
# getAge(-4)       # 年龄不能为负,若是负数  归零

# 为getAge添加一个功能,如果年龄为负,那么设置为0

# 如果装饰器带参,那么多两个步骤
# 1.给inner添加一个参数
# 2.将这个参数放到fn()中

def outer(fn):
    def inner(age):  # 如果装饰器要带参,那么参数要写成闭包inner的形参
        # 新增功能
        if age < 0:
            age = 0  # 校正之后再执行getAge函数

        fn(age)  # 放参

    return inner


f = outer(getAge)  # getAge -->fn  fn() -->getAge()

f(10)  # 10   inner(10)
f(-5)  # 0    inner(-5) --> getAge(0)


# 语法糖： @outer是一个语法糖，本质上操作并没有改变，还是让程序员用起来更方便
def getAge(age):
    print(age)


# 装饰器
def outer(fn):
    def inner(age):
        if age < 0:
            age = 0
        fn(age)

    return inner


@outer  # 使用@（语法糖） 装饰器修饰这个函数，这个函数新增功能就在outer中
def getAge(age):
    print(age)


# 每次使用装饰器，都要获取闭包，再来调用闭包，比较麻烦，python提供了简化方法
f = outer(getAge)
f(10)  # 10
f(-5)  # 0

# 修饰后
getAge(10)  # 10  -->  f = outer(getAge)  -->f(10)
getAge(-5)  # 0


# 不定长参数装饰器
def wrapper(fn):
    def inner(*args):  # 闭包接收不定长参数

        print("hello world")

        fn(*args)  # 将这个不定长参数，同样给fn函数

    return inner


@wrapper  # 上面这个装饰器的功能就是多打印了一句hello world
def show(a, b):
    print(a + b)


show(3, 4)  # hello world    7    闭包中多加的功能 + 函数原有的功能


@wrapper
def show2(a, b, c, d):
    print(a, b, c, d)


show2("hello", "world", "adsa", "sdasd")


# 多个装饰器作用于同一函数
def wrapper(fn):
    def inner():
        print("11111")
        fn()

    return inner


def wrapper2(fn):
    def inner():
        print("111112222")
        fn()

    return inner


@wrapper
@wrapper2  # 多个装饰器可以修饰同一个函数,装饰器新增的功能都会执行
# 但是原函数只会被执行一次
#
def show():  # 原函数有参,则装饰器inner就带参
    print("秀")


show()  # 只会打出一个秀!
