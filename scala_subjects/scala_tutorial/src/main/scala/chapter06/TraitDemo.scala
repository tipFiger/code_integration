package chapter06

/*
* Scala基础语法
* Scala Trait(特征) 相当于 Java 的接口，实际上它比接口还功能强大。接口不同的是，它还可以定义属性和方法的实现。
* Scala的类只能够继承单一父类，但是如果是 Trait(特征) 的话就可以继承多个，从结果来看就是实现了多重继承。
*
* */
trait Equal {
  def isEqual(x: Any): Boolean
  def isNotEqual(x: Any): Boolean = !isEqual(x)
}

class PointT(xc: Int, yc: Int) extends Equal {
  var x: Int = xc
  var y: Int = yc
  def isEqual(obj: Any) =
    obj.isInstanceOf[Point] &&
      obj.asInstanceOf[Point].x == x
}

object Test {
  def main(args: Array[String]) {
    val p1 = new PointT(2, 3)
    val p2 = new PointT(2, 4)
    val p3 = new PointT(3, 3)

    println(p1.isNotEqual(p2))
    println(p1.isNotEqual(p3))
    println(p1.isNotEqual(2))
  }
}

// 构造器的执行顺序：
//   调用超类的构造器；
//   特征构造器在超类构造器之后、类构造器之前执行；
//   特征由左到右被构造；
//   每个特征当中，父特征先被构造；
//   如果多个特征共有一个父特征，父特征不会被重复构造
//   所有特征被构造完毕，子类被构造。
