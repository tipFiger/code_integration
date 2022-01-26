# -*- coding:utf8 -*-
"""
@author:natural
@file:33_正则表达式.py
@time:2022/01/24
"""
# re 模块使 Python 语言拥有全部的正则表达式功能

# re.findall(pattern, string[, flags]) 字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回
import re

# 设定一个常量
a = 'x|twowater|liangdianshui|草根程序员|ReadingWithU'

# 正则表达式

findall = re.findall('x', a)
print(findall)

if len(findall) > 0:
    print('a 含有“x”这个字符串')
else:
    print('a 不含有“x”这个字符串')

# 方括号 “[]” 里面的字符关系是"或（OR）"关系
import re

a = 'uav,ubv,ucv,uwv,uzv,ucv,uov'

# 字符集

# 取 u 和 v 中间是 a 或 b 或 c 的字符
findall = re.findall('u[abc]v', a)
print(findall)
# 如果是连续的字母，数字可以使用 - 来代替
l = re.findall('u[a-c]v', a)
print(l)

# 取 u 和 v 中间不是 a 或 b 或 c 的字符
re_findall = re.findall('u[^abc]v', a)
print(re_findall)

# 正则表达式本身就定义了一些规则，比如 \d,匹配所有数字字符,其实它是等价于 [0-9]
import re

a = 'uav_ubv_ucv_uwv_uzv_ucv_uov&123-456-789'

# 概括字符集

# \d 相当于 [0-9] ,匹配所有数字字符
# \D 相当于 [^0-9] ， 匹配所有非数字字符
findall1 = re.findall('\d', a)
findall2 = re.findall('[0-9]', a)
findall3 = re.findall('\D', a)
findall4 = re.findall('[^0-9]', a)
print(findall1)
print(findall2)
print(findall3)
print(findall4)

# \w 匹配包括下划线的任何单词字符，等价于 [A-Za-z0-9_]
findall5 = re.findall('\w', a)
findall6 = re.findall('[A-Za-z0-9_]', a)
print(findall5)
print(findall6)

# 数量词的词法是：{min,max} 。min 和 max 都是非负整数
import re

a = 'java*&39android##@@python'

# 数量词

findall = re.findall('[a-z]{4,7}', a)
print(findall)

# 贪婪模式：它的特性是一次性地读入整个字符串，如果不匹配就吐掉最右边的一个字符再匹配，直到找到匹配的字符串或字符串的长度为 0 为止。它的宗旨是读尽可能多的字符，所以当读到第一个匹配时就立刻返回。
#
# 懒惰模式：它的特性是从字符串的左边开始，试图不读入字符串中的字符进行匹配，失败，则多读一个字符，再匹配，如此循环，当找到一个匹配时会返回该匹配的字符串，然后再次进行匹配直到字符串结束。
# ?：告诉引擎匹配前导字符 0 次或 1 次
# +：告诉引擎匹配前导字符 1 次或多次
# *：告诉引擎匹配前导字符 0 次或多次

import re

a = 'java*&39android##@@python'

# 贪婪与非贪婪

re_findall = re.findall('[a-z]{4,7}?', a)
print(re_findall)

# 贪 婪	惰 性	描 述
# ？	？？	零次或一次出现，等价于{0,1}
# +	+？	一次或多次出现 ，等价于{1,}
# *	*？	零次或多次出现 ，等价于{0,}
# {n}	{n}？	恰好 n 次出现
# {n,m}	{n,m}？	至少 n 次枝多 m 次出现
# {n,}	{n,}？	至少 n 次出现

# 分组，被括号括起来的表达式就是分组


# re.sub 共有五个参数。其中三个必选参数：pattern, repl, string ; 两个可选参数：count, flags .


import re

a = 'Python*Android*Java-888'

# 把字符串中的 * 字符替换成 & 字符
sub1 = re.sub('\*', '&', a)
print(sub1)

# 把字符串中的第一个 * 字符替换成 & 字符
sub2 = re.sub('\*', '&', a, 1)
print(sub2)


# 把字符串中的 * 字符替换成 & 字符,把字符 - 换成 |

# 1、先定义一个函数
def convert(value):
    group = value.group()
    if (group == '*'):
        return '&'
    elif (group == '-'):
        return '|'


# 第二个参数，要替换的字符可以为一个函数
sub3 = re.sub('[\*-]', convert, a)
print(sub3)

# re.match 函数
#
# 语法：
#
# re.match(pattern, string, flags=0)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。
#
# re.search 函数
#
# 语法：
#
# re.search(pattern, string, flags=0)
# re.search 扫描整个字符串并返回第一个成功的匹配。

import re

a = '<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'

# 使用 re.search
search = re.search('<img src="(.*)">', a)
# group(0) 是一个完整的分组
print(search.group(0))
print(search.group(1))

# 使用 re.findall
findall = re.findall('<img src="(.*)">', a)
print(findall)

# 多个分组的使用（比如我们需要提取 img 字段和图片地址字段）
re_search = re.search('<(.*) src="(.*)">', a)
# 打印 img
print(re_search.group(1))
# 打印图片地址
print(re_search.group(2))
# 打印 img 和图片地址，以元祖的形式
print(re_search.group(1, 2))
# 或者使用 groups
print(re_search.groups())
