package chapter07

/*
* scala基础语法
* 集合 Scala 集合分为可变的和不可变的集合。
* list
* set
* map
* 元组
* Option
* Iterator（迭代器）
* */
object CollectionDemo {
  def main(args: Array[String]): Unit = {
    // 定义整型 List
    val x1 = List(1, 2, 3, 4)

    // 定义 Set
    val x2 = Set(1, 3, 5, 7)

    // 定义 Map
    val x3 = Map("one" -> 1, "two" -> 2, "three" -> 3)

    // 创建两个不同类型元素的元组
    val x4 = (10, "Runoob")

    // 定义 Option
    val x5: Option[Int] = Some(5)

    println(x1)
    println(x2)
    println(x3)
    println(x4)
    println(x5)

  }
}
