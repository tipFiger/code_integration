package chapter09

/*
* Scala基础语法
* 提取器 是从传递给它的对象中提取出构造该对象的参数
* Scala 提取器是一个带有unapply方法的对象。unapply方法算是apply方法的反向操作：unapply接受一个对象，然后从对象中提取值，提取的值通常是用来构造该对象的值。
*
* */
object ExtractorDemo {
  def main(args: Array[String]): Unit = {
    println("Apply 方法 : " + apply("Zara", "gmail.com"));
    println("Unapply 方法 : " + unapply("Zara@gmail.com"));
    println("Unapply 方法 : " + unapply("Zara Ali"));

    // 
    val x = Test11(5)
    println(x)

    x match
    {
      case Test11(num) => println(x + " 是 " + num + " 的两倍！")
      //unapply 被调用
      case _ => println("无法计算")
    }

  }

  // 注入方法 (可选)
  def apply(user: String, domain: String) = {
    user + "@" + domain
  }

  // 提取方法（必选）
  def unapply(str: String): Option[(String, String)] = {
    val parts = str split "@"
    if (parts.length == 2) {
      Some(parts(0), parts(1))
    } else {
      None
    }
  }

  // 提取器使用匹配模式
  def apply(x: Int) = x*2
  def unapply(z: Int): Option[Int] = if (z%2==0) Some(z/2) else None
  case class Test11(i: Int)

}
