package chapter06

/*
* Scala基础语法
* 使用object创建单例对象
* Scala 中使用单例模式时，除了定义的类之外，还要定义一个同名的 object 对象，它和类的区别是，object对象不能带参数。
* */

import java.io._

class Point1(val xc1: Int, val yc1: Int) {
  var x: Int = xc1
  var y: Int = yc1

  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
  }
}

object SingletonDemo {
  def main(args: Array[String]): Unit = {
    val point = new Point1(10, 20)
    printPoint

    def printPoint {
      println("x 的坐标点 : " + point.x);
      println("y 的坐标点 : " + point.y);
    }
  }
}
