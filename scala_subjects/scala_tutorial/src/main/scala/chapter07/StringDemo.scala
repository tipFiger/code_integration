package chapter07

/*
* Scala基础语法
* 字符串的使用
*
* */
object StringDemo {
  // 创建字符串
  val greeting: String = "Hello, World!"

  def main(args: Array[String]): Unit = {
    // 打印字符串
    println(greeting)

    // String对象不可变，需要创建一个可以修改的字符串，可以使用 String Builder 类
    val buf = new StringBuilder
    buf += 'a'
    buf ++= "bcdef"
    println("buf is : " + buf.toString)

    // 使用 length() 方法来获取字符串长度
    val palindrome: String = "www.runoob.com"
    val len: Int = palindrome.length
    println("String Length is : " + len)

    // 使用 concat() 方法来连接两个字符串
    val str1: String = "x："
    val str2: String = "www.x.com"
    val str3: String = "x Slogan 为："
    val str4: String = "学的不仅是技术，更是梦想！"
    println(str1 + str2)
    println(str3.concat(str4))

    //  printf() 方法来格式化字符串并输出，String format() 方法可以返回 String 对象而不是 PrintStream 对象
    var floatVar = 12.456
    var intVar = 2000
    var stringVar = "x!"
    var fs = printf("浮点型变量为 " +
      "%f, 整型变量为 %d, 字符串为 " +
      " %s", floatVar, intVar, stringVar)
    println(fs)
  }
}
