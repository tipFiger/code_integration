package chapter04

/*
* Scala基础语法
* for循环
* while循环
* do while循环
*
* */
object LoopDemo {
  def main(args: Array[String]): Unit = {
    // for循环
    var a = 0
    for (a <- 1 to 10) {
      println("Value of a1:" + a)
    }

    // while循环
    while ( {
      a < 20
    }) {
      println("Value of a: " + a)
      a = a + 1
    }

    // do while 循环
    do {
      println("Value of a: " + a)
      a = a + 1
    } while ( {
      a < 20
    })

  }

}
