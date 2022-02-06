package chapter06

/*
* Scala基础语法
* 类 是对象的抽象
* 对象是类的具体实例（实例化）
*
* */

// 抽象一个类
class Point(xc: Int, yc: Int) {
  var x: Int = xc
  var y: Int = yc

  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
    println("x 的坐标点: " + x);
    println("y 的坐标点: " + y);
  }
}

// 实例化调用
object ClassObjectDemo {
  def main(args: Array[String]): Unit = {
    val pt = new Point(10, 20)

    // 移到一个新的位置
    pt.move(10, 10)

    // 继承后的类的使用 移到一个新的位置
    val loc = new Location(10, 20, 15)
    loc.move(10, 10, 5)

    //



  }
}

// 继承
// 1、重写一个非抽象方法必须使用override修饰符。
// 2、只有主构造函数才可以往基类的构造函数里写参数。
// 3、在子类中重写超类的抽象方法时，你不需要使用override关键字。
class Location(val xc: Int, val yc: Int,
               val zc: Int) extends Point(xc, yc) {
  var z: Int = zc

  def move(dx: Int, dy: Int, dz: Int) {
    x = x + dx
    y = y + dy
    z = z + dz
    println("x 的坐标点 : " + x);
    println("y 的坐标点 : " + y);
    println("z 的坐标点 : " + z);
  }
}
