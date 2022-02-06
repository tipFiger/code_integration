package chapter06

/*
* 伴生对象
*
* */

// 私有构造方法
class CompanionDemo private(val color: String) {

  println("创建" + this)

  override def toString(): String = "颜色标记：" + color

}

// 伴生对象，与类名字相同，可以访问类的私有属性和方法
object CompanionDemo {

  private val markers: Map[String, CompanionDemo] = Map(
    "red" -> new CompanionDemo("red"),
    "blue" -> new CompanionDemo("blue"),
    "green" -> new CompanionDemo("green")
  )

  def apply(color: String) = {
    if (markers.contains(color)) markers(color) else null
  }


  def getMarker(color: String) = {
    if (markers.contains(color)) markers(color) else null
  }

  def main(args: Array[String]) {
    println(CompanionDemo("red"))
    // 单例函数调用，省略了.(点)符号
    println(CompanionDemo getMarker "blue")
  }
}
