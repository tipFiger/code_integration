# -*- coding:utf8 -*-
"""
@author:natural
@file:34_文件读写.py
@time:2022/01/24
"""
# 文件处理
# 文件的处理包括读文件和写文件，读写文件就是请求操作系统打开一个文件对象，然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
#
# 2.1 文件读取
# 文件读取可分为以下步骤：
#
# 打开文件
# 读取文件内容
# 关闭文件
# 打开文件要使用open内建函数：
#
# open(file [, mode='r', encoding=None, errors=None])
#
# 参数说明： file：文件路径，可以是相对路径和绝对路径
#
# ​ mode：文件打开模式
#
# 	    encodeing: 文件编码方式，不用于二进制文件，一般是utf-8,gbk
# ​ errors：指定如何处理编码和解码错误 ，适用于文本文件
#
# 返回值：一个可迭代的文件对象
#
# mode	解释
# r	只读
# w	写之前会清空文件的内容，如果文件不存在，会创建新文件
# a	追加的方式，在原本内容中继续写，如果文件不存在，则会创建新文件
# r+	可读可写
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# b	rb、wb、ab、rb+、wb+、ab+意义和上面一样，用于二进制文件操作
# 注意：二进制文件一般用于视频、音频、图片
#
# 读取文件常用函数：
#
# 函数	解释
# read([size])	读取文件(读取size字节，默认读取全部)
# readline([size])	读取一行,如果指定size，将读入指定的字符数
# readlines()	把文件内容按行全部读入，返回一个包含所有行的列表
#  #打开文件
# fp = open('qfile.txt','r',encoding='utf-8')
#
# #读取文件全部内容
# #content = fp.read()
# #print(content)
#
# #读取指定字符数,包括行尾的换行符\n
# # print(fp.read(20))
#
# #读取一行
# # print(fp.readline(5))  #读取指定字符数
# # print(fp.readline())  #读取一整行，直到碰到一个\n
#
# #读取所有行，返回列表
# # print(fp.readlines())
#
#  #关闭文件
# fp.close()
# #由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# # 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# # try:
# #     fp = open('qfile.txt','r',encoding='utf-8')
# #     print(fp.readlines())
# # finally:
# #     fp.close()
# #可以简写为：
# #with语句会自动调用close方法关闭文件
# with open('qfile.txt','r',encoding='utf-8')  as fp:
#     print(fp.readline())
# #fread()和freadlines()会一次读入文件全部内容，如果文件太大，会直接耗尽内存的，因为文件对象可迭代，所以可以用for循环遍历文件读取
# with open('qfile.txt','r',encoding='utf-8')  as fp:
#     for line in fp:
#         print(line.strip())   #注意无论是read、readline、readlines都会读入行末的\n，所以需要手动剔除\n
# 2.2 写文件
# path = "file11.txt"
#
# #1.打开文件
# f = open(path,"w",encoding="utf-8")
#
# #2.写入内容，将内容写入到缓冲区
# #不会自动换行，需要换行的话，需要在字符串末尾添加换行符
# f.write("Whatever is worth doing is worth doing well该行很骄傲很关键\n")
#
#
# #3.刷新缓冲区【加速数据的流动，保证缓冲区的流畅】
# f.flush()
#
# #4.关闭文件  关闭文件也会刷新缓冲区
# f.close()
#
# #简写方式：可以不用手动调用close
# with open(path,"w",encoding="utf-8") as f1:
#     f.write("Whatever is worth doing is worth doing well该行很骄傲很关键")
# 2.3 移动文件指针
# 文件是顺序向后读写的，如果想要移动文件指针，可以使用seek方法：
#
# file_obj.seek(offset,whence=0)
#
# 功能：移动文件指针
#
# 参数：offset 是偏移量，正数表示从文件开头向文件末尾移动，负数相反。
#
# ​ whence ： 文件指针的位置，可选参数，值可以是
#
# ​ SEEK_SET or 0 表示文件开头位置，是默认值
#
# ​ SEEK_CUR or 1 表示当前位置（不能使用）
#
# ​ SEEK_END or 2 文件末尾位置(不能使用)
#
# 返回值：无
#
# #1.txt内容：hello world
# with open('1.txt','r',encoding='utf-8') as fp:
#     fp.seek(5)  #移动到hello后的空格位置
#     print(fp.read(3))  #wo
#     fp.seek(0)   #移动到开头
#     print(fp.read(5))  #hello
#     print(fp.tell())   #tell()显示当前指针位置
# 2.4编码和解码
# 字符串类型和字节类型转换过程
#
# ​ 字符串类型转换为字节类型：编码，encode
#
# ​ 字节类型转换为字符串类型：解码，decode
#
# str = "今天是个好日子 today is a good day"
# path = "file22.txt"
#
# with open(path,"wb") as f:
#     result = str.encode("utf-8")
#     print(result)
#     f.write(result)
#
# with open(path,"rb") as f1:
#     data = f1.read()
#     print(data)
#     print(type(data))
#
#     newData = data.decode("utf-8")
#     print(newData)
#     print(type(newData))
# 3.CSV文件操作
# 逗号分隔值（Comma-Separated Values，CSV），其文件以纯文本形式存储表格数据（数字和文本），文件的每一行都是一个数据记录。每个记录由一个或多个字段组成，用逗号分隔。使用逗号作为字段分隔符是此文件格式的名称的来源，因为分隔字符也可以不是逗号，有时也称为字符分隔值。
#
# 在Windows下，csv文件可以通过记事本，excel，notepad++,editplus等打开
#
# 作用：CSV广泛用于不同体系结构的应用程序之间交换数据表格信息，解决不兼容数据格式的互通问题。
# 需要导入csv模块
# 3.1 读取csv
# import csv
# with open(r'csv\winequality-red.csv') as fp:  #1.打开文件
#     #delimiter指定分隔符
#     csv_reader = csv.reader(fp,delimiter=';')  #2.获取csv读取器
#     header = next(csv_reader) #获取第一行的标题
#     print(header)
#     for line in csv_reader: #3.遍历所有的行
#         print(line)
# 3.2 写入csv
# import csv
# l1 = [[1,2,3],[4,5,6],[7,8,9]]
# #打开文件时，要添加newline=''参数，否则会多一个空行
# with open('1.csv','w',newline='') as fp: #1.打开文件
# 	#delimiter='\t'指定数据分隔符
#     csv_writer = csv.writer(fp,delimiter='\t')  #2.获取writer
#     for line in l1:
#         csv_writer.writerow(line)  #3.写入文件
# 4.数据的持久化
# ​ 数据持久化就是将内存中的对象转换为存储模型,以及将存储模型转换为内存中的对象的统称. 对象可以是任何数据结构或对象模型,存储模型可以是关系模型、XML、二进制流等
#
# Python的数据持久化操作主要是六类：普通文件、DBM文件、Pickled对象存储、shelve对象存储、对象数据库存储、关系数据库存储。
#
# 4.1 pickled
# pickled可以将所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。以及由任何原生类型组成的列表，元组，字典和集合；函数，类，类的实例保存到文件
#
# dump 将对象保存到文件
#
# pickle.dump(obj, file[, protocol])
# 参数的含义分别为：
# obj: 要持久化保存的对象；
# file: 一个拥有 write() 方法的对象，并且这个 write() 方法能接收一个字符串作为参数。这个对象可以是一个以写模式打开的文件对象或者一个 StringIO 对象，或者其他自定义的满足条件的对象。
# protocol: 这是一个可选的参数，默认为 0 ，如果设置为 1 或 True，则以高压缩的二进制格式保存持久化后的对象，否则以ASCII格式保存。
# load 从文件中读取数据，还原成对象
#
# pickle.load(file)
#  只有一个参数 file ，对应于上面 dump 方法中的 file 参数。这个 file 必须是一个拥有一个能接收一个整数为参数的 read() 方法以及一个不接收任何参数的 readline() 方法，并且这两个方法的返回值都应该是字符串。这可以是一个打开为读的文件对象、StringIO 对象或其他任何满足条件的对象。
# import pickle
# tmp = [10,20,30]
# #必须以二进制方式打开
# with open("test1.data",'wb') as fp:
#     pickle.dump(tmp,fp)
#
# #必须以二进制方式打开
# with open('test1.data','rb') as fp:
#     t2 = pickle.load(fp)
# print(t2)
# 4.2 dbm
# 在一些python小型应用程序中，不需要关系型数据库时，可以方便的用持久字典来存储名称/值对，它与python的字典非常类似，主要区别在于数据是在磁盘读取和写入的。另一个区别在于dbm的键和值必须是字符串类型。
#
# dbm.open(file, flag='r', mode=0o666)
#
# 参数：
#
# ​ file 数据库文件名
#
# ​ flag 打开方式
#
# 值	含义
# 'r'	打开现有数据库以进行只读（默认）
# 'w'	打开现有数据库进行读写
# 'c'	打开用于读取和写入的数据库，如果不存在则创建它
# 'n'	始终创建一个新的空数据库，打开进行读取和写入
# import dbm
# #写入数据库
# # with dbm.open('test4','c') as db:
# #     db['name'] = b"tom"
# #     db['gender'] = '男'.encode('utf-8')
#
# #读取数据库内容
# with dbm.open('test4') as db:
#    for value in db:
#        print(db[value].decode('utf-8'))
# 4.3 shelve
# shelve是一个持久的，类似字典的对象。与dbm数据库的区别是，值（而不是键！）可以是基本上任意的Python对象 ,可以处理的任何东西。这包括大多数类实例，递归数据类型和包含大量共享子对象的对象。键是普通字符串。
#
# shelve.open(filename, flag='c', protocol=None, writeback=False)
#
# 参数：
#
# ​ filename 数据库文件名
#
# ​ flag 打开方式，同dbm相同
#
# ​ protocol 同dbm
#
# ​ wirteback 写回，如果修改了对象是否写回到数据库文件
#
# import shelve
# #写入数据
# # with shelve.open('test5',flag='c') as db:
# #     #直接把db当做字典操作就可以了
# #     db['a'] = [10,20]
# #     db['b'] = 30
# #     db['c'] = 'hello'
#
#
# #读取
# with shelve.open('test5') as db:
#    for key in db:
#        print(key,db[key])
#
# #修改
# # with shelve.open('test5',writeback=True) as db:
# #    db['a'].append(30)
# #    del db['b']
