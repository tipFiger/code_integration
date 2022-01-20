# -*- coding:utf8 -*-
"""
@author:natural
@file:14_条件语句.py
@time:2022/01/19
"""
# 通过一条或多条语句的执行结果（ True 或者 False ）来决定执行的代码块 if语句的关键字为：if – elif – else。
# if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。
results = 59
if results >= 60:
    print('及格')
else:
    print('不及格')

# if 语句多个判断条件
results = 89
if results > 90:
    print('优秀')
elif results > 80:
    print('良好')
elif results > 60:
    print('及格')
else:
    print('不及格')

# if 语句多个条件同时判断 or （或）表示两个条件有一个成立时判断条件成功  and （与）表示只有两个条件同时成立的情况下，判断条件才成功。
java = 86
python = 68
if java > 80 and python > 80:
    print('优秀')
else:
    print('不优秀')

if (java >= 80 and java < 90) or (python >= 80 and python < 90):
    print('良好')

# if 嵌套
java = 86
python = 68
if java > 80:
    if python > 80:
        print('优秀')
    else:
        print('不优秀')
else:
    print('不优秀')  # 这里不会走
