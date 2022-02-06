package chapter04

/*
* Scala基础语法
* if条件语句 if 语句有布尔表达式及之后的语句块组成
*
*
* */
object IfElseDemo {
  def main(args: Array[String]): Unit = {
    // if .. else if .. else
    val a1 = 30
    if (a1 < 20) {
      println("该变量小于20")
    } else if (a1 == 10) {
      println("该变量等于10")
    } else {
      println("该值大于20")
    }

    // if .. else 嵌套语句
    val x: Int = 30
    val y: Int = 10
    if (x == 30) {
      if (y == 10) {
        println("X = 30 , Y = 10")
      }
    }
  }
}
