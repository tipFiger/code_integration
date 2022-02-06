package chapter03

/*
* scala基础语法
* 算术运算符
* 关系运算符
* 逻辑运算符
* 位运算符
* */
object OperatorDemo {
  def main(args: Array[String]): Unit = {

    val a: Int = 10
    val b: Int = 20
    val c: Int = 25
    val d: Int = 25
    // 算数运算符
    println("a + b = " + (a + b))
    println("a - b = " + (a - b))
    println("a * b = " + (a * b))
    println("b / a = " + (b / a))
    println("b % a = " + (b % a))
    println("c % a = " + (c % a))

    // 关系运算符
    println("a == b = " + (a == b))
    println("a != b = " + (a != b))
    println("a > b = " + (a > b))
    println("a < b = " + (a < b))
    println("b >= a = " + (b >= a))
    println("b <= a = " + (b <= a))

    // 逻辑运算符
    val a1: Boolean = true
    val b1: Boolean = false
    println("a1 && b1 = " + (a1 && b1))
    println("a1 || b1 = " + (a1 || b1))
    println("!(a1 && b1) = " + !((a1 && b1)))

    // 按位运算
    val a2 = 60
    /* 60 = 0011 1100 */
    val b2 = 13
    /* 13 = 0000 1101 */
    var c2 = 0
    c2 = a2 & b2 /* 12 = 0000 1100 */
    println("a2 & b2 = " + c2)
    c2 = a2 | b2 /* 61 = 0011 1101 */
    println("a2 | b2 = " + c2)
    c2 = a2 ^ b2 /* 49 = 0011 0001 */
    println("a2 ^ b2 = " + c2)
    c2 = ~a2 /* -61 = 1100 0011 */
    println("~a2 = " + c2)
    c2 = a2 << 2 /* 240 = 1111 0000 */
    println("a2 << 2 = " + c2)
    c2 = a2 >> 2 /* 215 = 1111 */
    println("a2 >> 2  = " + c2)
    c2 = a2 >>> 2 /* 215 = 0000 1111 */
    println("a2 >>> 2 = " + c2)
  }
}
