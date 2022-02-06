package chapter08

import scala.util.matching.Regex

/*
* Scala基础语法
* 正则表达式
*  scala.util.matching 包中的 Regex 类来支持正则表达式
* */
object RegexDemo {
  def main(args: Array[String]): Unit = {
    // findFirstIn 找到首个匹配项
    val pattern1 = "Scala".r
    val str1 = "Scala is Scalable and cool"

    println(pattern1 findFirstIn str1)

    // findAllIn 查看所有的匹配项
    val pattern2 = new Regex("(S|s)cala") // 首字母可以是大写 S 或小写 s
    val str2 = "Scala is scalable and cool"

    println((pattern2 findAllIn str2).mkString(",")) // 使用逗号 , 连接返回结果

    //  replaceFirstIn( ) 方法来替换第一个匹配项
    val pattern3 = "(S|s)cala".r
    val str3 = "Scala is scalable and cool"

    println(pattern3 replaceFirstIn(str3, "Java"))

    // replaceAllIn( ) 方法替换所有匹配项
    val pattern4 = "(S|s)cala".r
    val str4 = "Scala is scalable and cool"

    println(pattern4 replaceAllIn(str4, "Java"))

  }
}
