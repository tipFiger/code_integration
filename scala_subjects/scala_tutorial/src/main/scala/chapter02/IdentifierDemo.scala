package chapter02

import chapter01.Student

/*
* scala基本语法：动态类型
* 变量 var 变量名[:变量类型] = 初始化值
* 常量 val 变量名[:变量类型] = 初始化值
* 变量和常量的类型可以不写 能用常量的地方尽量不用变量
* 标识符：自己命名的都叫
* */
object IdentifierDemo {
  def main(args: Array[String]): Unit = {
    // 声明一个变量
    var a: Int = 10

    // 省略变量类型, 编译器自动推导（类型推导）
    var a1 = 10
    val b1 = 13

    // 类型确定之后不能修改（Scala是强类型语言）
    var a2 = 15 // a2是个Int型
    //    a2 = "a" 会报错

    // 声明的时候需要有初始值
    // var a3: Int  会报错

    // 声明变量可以用var或者val修饰，var修饰的可以改变，val修饰的值不可以改变
    a1 = 12
    // b1 = 25 会报错

    // 引用类型
    var alice1 = new Student("alice", age = 20)
    alice1 = new Student("Alice", age = 20)
    alice1 = null
    val alice = new Student("alice", age = 20)
    // alice = new Student("Alice", age = 20) 会报错
    val bob = new Student("bob", age = 10)
    bob.age = 24 // 属性如果可修改引用的时候可以修改
    bob.printInfo()

    // 标识符：字母或者下划线开头，后面接字母数字下划线
    val hello: String = "a"
    val hello123: String = "a"
    val _a = 123
    // val h-b = ""  idea没报错， 运行会报错

    // 标识符：操作符开头，且只包含操作符  + - * / # ！
    val +-*/#! = "a"
    // val +-*/#!1 = "a" 会报错
    println(+-*/#!)

    // 用反引号包着的任意字符都可以作为标识符，哪怕是关键字
    val `if` = "if"
    println(`if`)
  }
}
