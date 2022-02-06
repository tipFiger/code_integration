package chapter07

/*
* Scala基础语法
* 迭代器 不是一个集合，它是一种用于访问集合的方法
* 迭代器 it 的两个基本操作是 next 和 hasNext。
* 调用 it.next() 会返回迭代器的下一个元素，并且更新迭代器的状态。
* 调用 it.hasNext() 用于检测集合中是否还有元素
* */
object IteratorDemo {
  def main(args: Array[String]): Unit = {
    // 简单的例子
    val it = Iterator("Baidu", "Google", "Runoob", "Taobao")

    while (it.hasNext) {
      println(it.next())
    }

    // 查找最大最小元素
    val ita = Iterator(20,40,2,50,69, 90)
    val itb = Iterator(20,40,2,50,69, 90)
    println("最大元素是：" + ita.max )
    println("最小元素是：" + itb.min )

    // 获取最大长度
    println("ita.size 的值: " + ita.size )
    println("itb.length 的值: " + itb.length )



  }
}
