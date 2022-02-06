package chapter02

/*
* Scala基础语法
* 类型转换
* 方法重载
*
* */
object DataTypeConversionDemo {
  def main(args: Array[String]): Unit = {
    // 自动类型转换
    // 自动提升原则，多种类型混合时，系统自动将所有数据类型转换位精度最大的类型
    val a1: Byte = 10
    val b1: Long = 2553
    val res1: Long = a1 + b1
    val res2: Int = (a1 + b1.toInt) // 强转
    println(res1)
    println(res2)

    // 精度大的赋值给精度小的数据会报错，反之会自动转换
    val a2: Byte = 10
    val b2: Int = a2
    // val a3: Byte = b2 报错

    // byte short 和char之间不能自动转换  先转为Int类型然后转为char
    val a4: Byte = 10
    val c3: Char = 'a'
    // val b4: Char = a4 会报错
    // val c4: Byte = c3 // 运行会报错
    // println(c4)

    // byte short char三者计算 需要先转为int
    val a5: Byte = 10
    val b5: Short = 10
    val c5: Char = 'a'
    val res5: Int = a5 + b5 + c5 // 如果res是Short会报错
    println(res5)

    // 强制类型转换
    // 高精度转低精度
    val a6: Int = 2.333.toInt // 会报错 2.333默认是Double
    println(a6) // 直接取整 不会四舍五入
    // 强转符就近有效，可以用小括号提升优先级
    val a7: Int = (2.6 + 3.7).toInt // 不加括号只能转一个还是报错  不加括号是5  加了括号是6
    println(a7)

    // 数值与String类型互转
    val n: Int = 27
    val s: String = n + "" // toString也行
    println(s)

    val m: Int = "12".toInt

  }
}
