# -*- coding:utf8 -*-
"""
@author:natural
@file:30_枚举类.py
@time:2022/01/24
"""
# 每个常量都是 class 里面唯一的实例
from enum import Enum
from types import MappingProxyType

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 遍历枚举类型
for name, member in Month.__members__.items():
    print(name, '---------', member, '----------', member.value)

# 直接引用一个常量
print('\n', Month.Jan)


# 枚举类通过 __members__ 遍历它的所有成员的方法 Enum 是继承元类 EnumMeta 的
class EnumMeta(type):
    """Metaclass for Enum"""

    @property
    def __members__(cls):
        """Returns a mapping of member name->value.
        This mapping lists all enum members, including aliases. Note that this
        is a read-only view of the internal mapping.
        """
        return MappingProxyType(cls._member_map_)


# 需要控制枚举的类型，那么我们可以 Enum 派生出自定义类来满足这种需要
from enum import Enum, unique

Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'


if __name__ == '__main__':
    print(Month.Jan, '----------',
          Month.Jan.name, '----------', Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '----------', member, '----------', member.value)

# Enum 类的枚举是不支持大小运算符的比较的：枚举成员不是有序的，所以它们只支持通过标识(identity) 和相等性 (equality) 进行比较。下面来看看 == 和 is 的使用
# from enum import Enum
#
#
# class User(Enum):
#     Twowater = 98
#     Liangdianshui = 30
#     Tom = 12
#
#
# Twowater = User.Twowater
# Liangdianshui = User.Liangdianshui
#
# print(Twowater == Liangdianshui, Twowater == User.Twowater)
# print(Twowater is Liangdianshui, Twowater is User.Twowater)
#
# try:
#     print('\n'.join('  ' + s.name for s in sorted(User)))
# except TypeError as err:
#     print(' Error : {}'.format(err))


# IntEnum 类进行枚举，就支持比较功能
import enum


class User(enum.IntEnum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 12


try:
    print('\n'.join(s.name for s in sorted(User)))
except TypeError as err:
    print(' Error : {}'.format(err))
