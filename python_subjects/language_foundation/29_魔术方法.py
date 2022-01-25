# -*- coding:utf8 -*-
"""
@author:natural
@file:29_魔术方法.py
@time:2022/01/24
"""


# 魔术方法："__" 双下划线包起来的方法，使用这些魔术方法，我们可以构造出优美的代码，将复杂的逻辑封装成简单的方法

# dir() 来列出类中所有的魔术方法
class Test(object):
    pass


if __name__ == '__main__':
    methods = dir(Test())
    for i in methods:
        print(i)


# 构造(__new__)和初始化(__init__) 通过 __init__(self) 的方法在实例化对象的时候，对属性进行设置
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('name', 23)


# 创建一个类的过程是分为两步的，一步是创建类的对象，还有一步就是对类进行初始化
# __new__ 是用来创建类并返回这个类的实例, 而__init__ 只是将传入的参数来初始化该实例.
# __new__ 在创建一个实例的过程中必定会被调用,但 __init__ 就不一定，比如通过 pickle.load 的方式反序列化一个实例时就不会调用 __init__ 方法。
# def __new__(cls) 是在 def __init__(self) 方法之前调用的，作用是返回一个实例对象。
# 还有一点需要注意的是：__new__ 方法总是需要返回该类的一个实例，而 __init__ 不能返回除了 None 的任何值
class Test(object):
    def __new__(cls, *args, **kwargs):
        # 打印 __new__方法中的相关信息
        print('调用了 def __new__ 方法')
        print(args)
        # 最后返回父类的方法
        return super(Test, cls).__new__(cls)

    def __init__(self, name, age):
        print('调用了 def __init__ 方法')
        self.name = name
        self.age = age


if __name__ == '__main__':
    usr = Test('name', 23)


class User(object):
    def __getattr__(self, name):
        print('调用了 __getattr__ 方法：该方法定义了你试图访问一个不存在的属性时的行为')
        return super(User, self).__getattr__(name)

    def __setattr__(self, name, value):
        print('调用了 __setattr__ 方法：定义了对属性进行赋值和修改操作时的行为')
        return super(User, self).__setattr__(name, value)

    def __delattr__(self, name):
        print('调用了 __delattr__ 方法：定义的是你删除属性时的行为')
        return super(User, self).__delattr__(name)

    def __getattribute__(self, name):
        print('调用了 __getattribute__ 方法： 定义了你的属性被访问时的行为，相比较，__getattr__ 只有该属性不存在时才会起作用')
        return super(User, self).__getattribute__(name)


if __name__ == '__main__':
    user = User()
    # 设置属性值，会调用 __setattr__
    user.attr1 = True
    # 属性存在,只有__getattribute__调用
    user.attr1
    try:
        # 属性不存在, 先调用__getattribute__, 后调用__getattr__
        user.attr2
    except AttributeError:
        pass
    # __delattr__调用
    del user.attr1


# 一个描述器是一个有“绑定行为”的对象属性 (object attribute)，它的访问控制被描述器协议方法重写，
# __get__(), __set__() , 和 __delete__()，方法的对象叫做描述器
# 默认对属性的访问控制是从对象的字典里面 (__dict__) 中获取 (get) , 设置 (set) 和删除 (delete)

# __get__() 和 __set__() 这些方法的调用
class User(object):
    def __init__(self, name='张三', sex='男'):
        self.sex = sex
        self.name = name

    def __get__(self, obj, objtype):
        print('获取 name 值')
        return self.name

    def __set__(self, obj, val):
        print('设置 name 值')
        self.name = val


class MyClass(object):
    x = User('张三', '男')
    y = 5


if __name__ == '__main__':
    m = MyClass()
    print(m.x)

    print('\n')

    m.x = '李四'
    print(m.x)

    print('\n')

    print(m.x)

    print('\n')

    print(m.y)


# __get__ 发挥了作用.
class Meter(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    meter = Meter()
    foot = Foot()


if __name__ == '__main__':
    d = Distance()
    print(d.meter, d.foot)
    d.meter = 1
    print(d.meter, d.foot)
    d.meter = 2
    print(d.meter, d.foot)


class FunctionalList:
    ''' 实现了内置类型list的功能,并丰富了一些其他方法: head, tail, init, last, drop, take'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 获取第一个元素
        return self.values[0]

    def tail(self):
        # 获取第一个元素之后的所有元素
        return self.values[1:]

    def init(self):
        # 获取最后一个元素之前的所有元素
        return self.values[:-1]

    def last(self):
        # 获取最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 获取所有元素，除了前N个
        return self.values[n:]

    def take(self, n):
        # 获取前N个元素
        return self.values[:n]


# 魔术方法	说明
# __cmp__(self, other)	如果该方法返回负数，说明 self < other; 返回正数，说明 self > other; 返回 0 说明 self == other 。强烈不推荐来定义 __cmp__ , 取而代之, 最好分别定义 __lt__, __eq__ 等方法从而实现比较功能。 __cmp__ 在 Python3 中被废弃了。
# __eq__(self, other)	定义了比较操作符 == 的行为
# __ne__(self, other)	定义了比较操作符 != 的行为
# __lt__(self, other)	定义了比较操作符 < 的行为
# __gt__(self, other)	定义了比较操作符 > 的行为
# __le__(self, other)	定义了比较操作符 <= 的行为
# __ge__(self, other)	定义了比较操作符 >= 的行为

class Number(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        print('__eq__')
        return self.value == other.value

    def __ne__(self, other):
        print('__ne__')
        return self.value != other.value

    def __lt__(self, other):
        print('__lt__')
        return self.value < other.value

    def __gt__(self, other):
        print('__gt__')
        return self.value > other.value

    def __le__(self, other):
        print('__le__')
        return self.value <= other.value

    def __ge__(self, other):
        print('__ge__')
        return self.value >= other.value


if __name__ == '__main__':
    num1 = Number(2)
    num2 = Number(3)
    print('num1 == num2 ? --------> {} \n'.format(num1 == num2))
    print('num1 != num2 ? --------> {} \n'.format(num1 == num2))
    print('num1 < num2 ? --------> {} \n'.format(num1 < num2))
    print('num1 > num2 ? --------> {} \n'.format(num1 > num2))
    print('num1 <= num2 ? --------> {} \n'.format(num1 <= num2))
    print('num1 >= num2 ? --------> {} \n'.format(num1 >= num2))



