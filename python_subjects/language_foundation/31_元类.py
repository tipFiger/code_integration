# -*- coding:utf8 -*-
"""
@author:natural
@file:31_元类.py
@time:2022/01/24
"""


# 类就是一组用来描述如何生成一个对象的代码段
class ObjectCreator(object):
    pass


def echo(ob):
    print(ob)


mObject = ObjectCreator()
print(mObject)

# 可以直接打印一个类，因为它其实也是一个对象
print(ObjectCreator)
# 可以直接把一个类作为参数传给函数（注意这里是类，是没有实例化的）
echo(ObjectCreator)
# 也可以直接把类赋值给一个变量
objectCreator = ObjectCreator
print(objectCreator)


# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
def printHello(self, name='Py'):
    # 定义一个打印 Hello 的函数
    print('Hello,', name)


# 创建一个 Hello 类
Hello = type('Hello', (object,), dict(hello=printHello))

# 实例化 Hello 类
h = Hello()
# 调用 Hello 类的方法
h.hello()
# 查看 Hello class 的类型
print(type(Hello))
# 查看实例 h 的类型
print(type(h))

# 元类就是用来创建类的。也可以换个理解方式就是：元类就是类的类。

# 整形
age = 23
print(age.__class__)
# 字符串
name = 'name'
print(name.__class__)


# 函数
def fu():
    pass


print(fu.__class__)


# 实例
class eat(object):
    pass


mEat = eat()

print(mEat.__class__)
print(age.__class__.__class__)
print(name.__class__.__class__)
print(fu.__class__.__class__)
print(mEat.__class__.__class__)


# type 就是内建的元类。也就是 Python 自带的元类。


# 元类的主要目的就是为了当创建类时能够自动地改变类。
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

    __metaclass__ = upper_attr


#  这会作用到这个模块中的所有类

class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)


# 输出:'bip'

# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)


class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

# 元类本身而言，它们其实是很简单的：
# 拦截类的创建
# 修改类
# 返回修改之后的类


# 元类就是深度的魔法，99% 的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
# 那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。
# 元类的主要用途是创建 API。一个典型的例子是 Django ORM。它允许你像这样定义：

# class Person(models.Model):
# name = models.CharField(max_length=30)
# age = models.IntegerField()
