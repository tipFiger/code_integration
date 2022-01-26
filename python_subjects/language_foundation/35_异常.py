# -*- coding:utf8 -*-
"""
@author:natural
@file:35_异常.py
@time:2022/01/24
"""
# 异常处理
# 错误指的是代码有语法问题，无法解释运行，必须改正后才能运行
#
# 如果代码没有语法问题，可以运行，但会出运行时的错误，例如除零错误，下标越界等问题，这种在运行期间检测到的错误被称为异常 ，出现了异常必须处理否则程序会终止执行，用户体验会很差。Phthon支持程序员自己处理检测到的异常。可以使用try - except语句进行异常的检测和处理
#
# 1.1
# try-except语句
# 语法：
# try:
#     【代码块A】  # 可能会出错误的代码    异常检测
#     except Exception1[ as e]:  # 异常处理
#     【代码块1】  # 异常处理代码
#     except Exception2[ as e]:  # 异常处理
#     【代码块2】  # 异常处理代码
#     ....
#     except Exceptionn[ as e]:  # 异常处理
#     【代码块n】  # 异常处理代码
#     [ else:]  # 可选，如果没有引发异常会执行
#     处理语句
#     [finally:]  # 无论如何都要执行的语句
#     处理语句
#     【后续语句】
#     执行流程：
#     1、首先执行try中【代码块A】，如果出现异常，立即终止代码执行，转而到except块中进行异常处理
#     2、异常处理except模块可以多个，从上往下匹配，如果能够匹配成功，立即执行相应的异常处理代码块，执行完毕后，不在往下匹配，转到3执行
#     3、执行异常处理完毕后，如果有finally字句则执行finally字句，如果没有则执行【后续语句】
#     4、如果匹配不到异常，有finally则执行finally，然后则抛出错误，终止程序执行。
#     5、如果没有异常，如果有else字句则执行else字句，执行完else后，有finally字句则执行，没有则执行【后续语句】
#     注意事项：
#     except匹配顺序从上到下
#     except语句书写要求：精确的类型往前放，模糊的，不精确的往后放
#     except不带任何类型，则匹配所有类型异常，应该放到最后，吞掉异常
#     可以将多种异常用元组的方式（异常类型1，异常类型2...异常类型n）书写，简化代码
#     except字句中e，是一个对象，打印它，会显示异常信息描述
#     try-except也可以捕获方法或函数中抛出的异常
#     所有异常类型都继承自BaseException，使用BaseException可以将异常一网打尽
#     finally字句中可以进行一些清理工作，比如关闭文件，数据库等工作
#     1.3
#     抛出异常
#     手动抛出一个指定类型的异常，无论是哪种异常类都可以带一个字符串参数，对异常进行描述。
#
#     raise不带参数会把错误原样抛出
#     try:
#         raise ZeroDivisionError('除0错误')
#         # raise ZeroDivisionError  #如果不想获取错误信息，可以不带参数
#     except ZeroDivisionError as e:
#         print(e)  # 除0错误
#     1.4
#     异常嵌套
#     在try块和excep块中还可以分别再嵌套try - except块
#
#     1.5
#     assert断言
#     ​ 语法：asser
#     条件[, 异常描述字符串]
#
#     ​ 执行流程：如果条件为假，则抛出AssertionError，条件为真，就当assert不存在
#
#     ​ 作用：对于可能出问题的代码，加上断言，方便问题排查
#
#     print('start')
#     num = int(input('请输入一个1~9的整数:'))
#     assert 0 < num < 9, 'num不在1~9'
#     print('end')
#     1.6
#     自定义异常类
#     如果系统异常类型满足不了业务需求，那么可以自己定义异常类来处理。
#
#     自己定义的异常类必须继承BaseException或Exception
#     步骤：
#     在自定义异常类的构造函数中，调用父类构造函数
#     重写__str__方法输出异常信息
#     编写异常处理方法处理异常
#
#
#     class CustomError(BaseException):  # 继承BaseException
#         def __init__(self, msg):
#             super().__init__()  # 调用父类初始化
#             self.msg = msg
#
#         # 重写__str__，输出异常信息
#         def __str__(self):
#             return self.msg
#
#         # 3.自定义异常处理方法
#         def handle_exception(self):
#             print('异常处理')
#
#
#     try:
#         raise CustomError('自定义异常')
#     except CustomError as e:
#         print(e)
