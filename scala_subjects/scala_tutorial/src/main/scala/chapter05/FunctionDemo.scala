package chapter05

import java.util.Date

/*
* Scala基础语法
* Scala 方法是类的一部分，而函数是一个对象可以赋值给一个变量。
* 换句话来说在类中定义的函数即是方法。
* 传值调用（call-by-value）：先计算参数表达式的值，再应用到函数内部；
* 传名调用（call-by-name）：将未计算的参数表达式直接应用到函数内部
* */
object FunctionDemo {
  def main(args: Array[String]): Unit = {
    // 函数传名调用 该方法在变量名和变量类型使用 => 符号来设置传名调用
    delayed(time)

    // 指定函数参数名 通过指定函数参数名，并且不需要按照顺序向函数传递参数（关键字参数）
    printInt(b = 5, a = 7)

    // 函数-可变参数 参数的类型之后放一个星号来设置可变参数(可重复的参数)
    printStrings("Runoob", "Scala", "Python")

    // 递归函数 函数可以调用它本身
    for (i <- 1 to 10)
      println(i + " 的阶乘为: = " + factorial(i))

    // 默认参数值 可以不需要传递参数，这时函数就会调用它的默认参数值，如果传递了参数，则传递值会取代默认值
    println("返回值 : " + addInt())

    // 高阶函数 函数 f 和 值 v 作为参数，而函数 f 又调用了参数 v 高阶函数（Higher-Order Function）就是操作其他函数的函数
    println(apply(layout, 10))

    // 内嵌函数 定义在函数内的函数称之为局部函数。
    println(factorial(0))
    println(factorial(1))
    println(factorial(2))
    println(factorial(3))

    // 匿名函数
    println("multiplier(1) value = " + multiplier(1))
    println("multiplier(2) value = " + multiplier(2))

    // 偏函数 不需要提供函数需要的所有参数，只需要提供部分，或不提供所需参数
    val date = new Date
    log(date, "message1")
    Thread.sleep(1000)
    log(date, "message2")
    Thread.sleep(1000)
    log(date, "message3")

    // 函数柯里化 将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参数为参数的函数。
    // def add(x:Int,y:Int)=x+y
    // 变形 def add(x:Int)(y:Int) = x + y
    val str1: String = "Hello, "
    val str2: String = "Scala!"
    println("str1 + str2 = " + strcat(str1)(str2))

  }

  // 函数传名调用
  def time() = {
    println("获取时间，单位为纳秒")
    System.nanoTime
  }

  def delayed(t: => Long) = {
    println("在 delayed 方法内")
    println("参数： " + t)
    t
  }

  // 指定函数参数名
  def printInt(a: Int, b: Int) = {
    println("Value of a : " + a)
    println("Value of b : " + b)
  }

  // 函数-可变参数
  def printStrings(args: String*) = {
    var i: Int = 0
    for (arg <- args) {
      println("Arg value[" + i + "] = " + arg)
      i = i + 1
    }
  }

  // 递归参数
  def factorial(n: BigInt): BigInt = {
    if (n <= 1)
      1
    else
      n * factorial(n - 1)
  }

  // 默认参数值
  def addInt(a: Int = 5, b: Int = 7): Int = {
    var sum: Int = 0
    sum = a + b

    return sum
  }

  // 高阶函数
  def apply(f: Int => String, v: Int) = f(v)

  def layout[A](x: A) = "[" + x.toString() + "]"

  // 内嵌函数
  def factorial(i: Int): Int = {
    def fact(i: Int, accumulator: Int): Int = {
      if (i <= 1)
        accumulator
      else
        fact(i - 1, i * accumulator)
    }

    fact(i, 1)
  }

  // 匿名函数
  var factor = 3
  val multiplier = (i: Int) => i * factor

  //def add2 = new Function1[Int,Int]{
  //    def apply(x:Int):Int = x+1;
  //}
  // 简写 var inc = (x:Int) => x+1

  // 偏函数
  def log(date: Date, message: String) = {
    println(date + "----" + message)
  }

  // 函数柯里化
  def strcat(s1: String)(s2: String) = {
    s1 + s2
  }

}
