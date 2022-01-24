# -*- coding:utf8 -*-
"""
@author:natural
@file:27_面向对象.py
@time:2022/01/24
"""


# 面向过程，看重的是解决问题的过程
# 面向对象是一种抽象，抽象是指用分类的眼光去看世界的一种方法
# 类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 对象：通过类定义的数据结构实例
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
# 多态：它是指对不同类型的变量进行相同的操作，它会根据对象（或类）类型的不同而表现出不同的行为。
# 封装性：“封装”就是将抽象得到的数据和行为（或功能）相结合，形成一个有机的整体（即类）；封装的目的是增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，一特定的访问权限来使用类的成员。
# 实例化: 使用类创建对象的过程

class Person():  # 类名的定义规则,只能是字母,数字,下划线,遵循驼峰原则
    # 类属性                # 首字母必须大写!(约定)
    name = "231"
    age = 0

    # 对象属性
    def __init__(self, name, age):  # 实例化对象时,才能访问
        self.name = name
        self.age = age

    # 对象方法
    def show(self):  # self指,当前对象,会代表等下实例产生的对象
        print("hello")

    # 类方法(装饰器)
    @classmethod
    def myPrint(cls):
        print("6666")


p = Person("yi", 12)  # 实例化Person,得到p对象  self -> p
p.show()  # 使用对象所有拥有的方法
print(p.name)
print(p.age)
print(Person.name)
print(Person.age)

# Person.show()            # 崩溃! 对象方法只能用对象来调用,不能用类调用

# 类属性： 直接写在类中, 可以用对象,和类名来调用, 是所有对象共有成员
# 对象属性： 在构造函数__int__中声明, 必须实例化才能访问属性
# 类方法： 通过类名直接调用的方法   @classmethod    也可以用对象来调用  p.myPrint()
# 对象方法： 通过对象调用的方法

# 类方法   可以用对象,和类名来调用
Person.myPrint()
p.myPrint()


# 通过同一个类,实例化出来的两个对象,他们所存储的地址不是同一个

class Person():
    name = "xiaoming"

    def show(self):
        print("show")


p1 = Person()  # p1是一个变量,指向堆内存中Person对象中的内存地址
p2 = Person()

print(id(p1))
print(id(p2))


class Person():
    def sayHello(self):
        print("hello")


# 动态绑定: 声明类时,没有指定的属性, 在生成对象之后,动态添加
p1 = Person()
p1.name = "xiaoming"  # 动态添加属性
p1.money = 1000
p1.age = 20
print(p1.name)

p1.sayHello()


# 限制绑定: 只能使用特定的属性, 如果是其他的属性, 则报错
class Person():
    # 限制这个类,只能使用这两个属性
    Person.__slots__ = ("name", "age")


# 只允许Person对象使用name,和age属性,使用其他的就会报错
p1 = Person()
p1.name = "zhangsan"
p1.age = 20


# p1.money = 1000    # 运行报错


# 构造方法
class Person():
    # 作用是: 进行数据的初始化
    # 调用时机: 当对象实例化时,自动被调用
    def __init__(self):
        print("构造方法被调用了")


# 如果自己不写__init__,那么系统会自动为你调用,然后在创建对象
# 如果自己写了__init__,那么实例化对象时,会调用自己写的构造方法

# 带参的构造函数
class Person2():
    # 类属性
    # name = ""
    # age = 0
    # def __init__(self):
    # 	# 在对象实例化时,为name和age赋值
    # 	name = "xiaoming"       # 这个name 只是__init__ 函数中的局部变量,
    # 							# 调用后会被释放,所以这个对象属性赋初值无效
    # 	age = 20
    def __init__(self, name, age):
        self.name = name  # 对象属性
        self.age = age


# 不定长参数构造函数
# def __init__(self,*args):


# p = Person()
# print( p.name)         # 空
# 如果构造函数有参数,实例化类时,必须带上一样的参数
p = Person2("小明", 20)
print(p.name)
print(p.age)

p2 = Person2("tony", 40)
print(p2.name)
print(p2.age)

# 总结:  构造函数在对象创建时,就会自动调用,它的作用就是为每个对象的属性赋值.


# 析构函数__del__: 与构造函数相反,当对象被销毁(释放)时,自动调用
# 构造函数__init__: 当对象创建时,自动调用

import time


class Person():
    def __init__(self):
        print("构造函数被调用")

    def __del__(self):  # 一般用于关闭数据库连接,关闭文件
        print("析构函数被调用")


p = Person()  # 实例化Person时,调构造函数
# 当模块运行完毕,p对象被释放,自动调用析构函数
# del p             # 对象被手动删除时,也会立刻调析构函数
time.sleep(3)


# 将对象的实例化,放在函数中,那么函数调用结束,对象也会被立刻销毁
def fn():
    p = Person()  # 实例化,生


fn()  # 死


# 类属性       类方法
# 对象属性     对象方法

class Person():
    # 类属性: 支持类名.类属性  和  对象.类属性
    name = "xiaoming"

    # 类方法: 支持   和  对象.类方法
    @classmethod
    def show(cls):
        print("hello")

    # 对象属性: 支持  对象.属性名
    def __init__(self, age, name):
        self.age = 20
        self.name = "xiaoming"

    # 对象方法: 支持  对象.方法名
    def myPrint(self):
        print("66666")


print(Person.name)  # 类名.类属性
print(Person.show)  # 类名.类方法

p2 = Person(18, 2000)
print(p2.age)  # 对象名.对象属性  20
p2.myPrint()  # 对象名.对象方法


# Person.myPrint(Person)


# public （公共）属性 和 private （私有）属性，这可以对属性进行访问控制
class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


if __name__ == '__main__':
    userInfo = UserInfo('x', 23, 347073565);
    # 打印所有属性
    print(dir(userInfo))
    # 打印构造函数中的属性
    print(userInfo.__dict__)
    print(userInfo.get_account())
    # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)


# 方法看成是类的属性的，那么方法的访问控制也是跟属性是一样的，也是没有实质上的私有方法
class User(object):
    def upgrade(self):
        pass

    def _buy_equipment(self):
        pass

    def __pk(self):
        pass















