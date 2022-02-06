package chapter02

import chapter01.Student

/*
* Scala基础语法：
* 基本数据类型
* 一切数据都是对象，都是Any的子类
* 数值类型 AnyVal
* 引用类型 AnyRef
* 隐式转换 低精度的值类型向高精度值类型自动转换
* 值类型Unit 对应Java的void表示没有返回值，Unit是一个数据类型，只有一个对象就是() Void不是数据类型，只是一个关键字
* 值类型StringOps
* Null是一个引用类型只有一个对象null  Unit是空值Null就表示空引用
* Nothing是所有类型的子类，一个函数灭有明确返回值的时候使用
* */
object BaseDataTypeDemo {
  def main(args: Array[String]): Unit = {
    // 整形 Byte 8位 、Short 16位 、 Int 32位 、 Long 64位 范围区间就是2的多少位次幂  补码的概念
    val a1: Byte = 127
    // val a1: Byte = 128 会报错
    val a2 = 12 // 默认的是Int类型
    val a3 = 15646167964161L // Int超长的时候加个L表示长整型

    val b1: Byte = 10
    val b2: Byte = 10 + 20 // 这个不会报错
    println(b2)

    // val b3: Byte = b2 + 20  // 这个会报错，需要做强制类型转换
    val b3: Byte = (b1 + 20).toByte
    println(b3)

    // 浮点类型 Double Float
    val f1 = 1.23456 // 默认Double
    val f2: Float = 1.23456f

    // 字符类型 Char 表示单个字符
    val c1: Char = 'a'
    println(c1)
    // 字符转移
    val c2: Char = '\\'
    println(c2)
    // ASCII🐎
    val c3: Int = c1
    println(c3)

    // 布尔类型 Boolean true和flase
    val isTrue: Boolean = true
    println(isTrue)

    // 空类型：控制Unit
    def m1(): Unit = {
      println("调用执行m1")
    }
    // 调用函数
    val a4 = m1()
    println(a4)  // a4 返回一个空括号
    // 空引用Null
    // val n: Int = null // 会报错, 值类型不能接收null
    var stu: Student = new Student("alice", age = 20)
    stu = null
    println(stu)
    // Nothing  要抛出异常 Nothing是任何类的子类
    def m2(n: Int): Int = {
      if (n == 0)
        throw new NullPointerException
      else
        return n
    }
    val b = m2(0)
    println(b) // 调用的时候抛出异常退出了

  }
}
