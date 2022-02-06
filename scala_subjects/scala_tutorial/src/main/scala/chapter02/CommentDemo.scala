package chapter02

/*
* scala基本语法：
* Scala的注释 ，简而言之和Java的一样
* */
object CommentDemo {
  /**
   * 这是文档注释: 方法或者类上使用
   * 这个是程序入口方法
   *
   * @param args 外部传入参数
   * */
  def main(args: Array[String]): Unit = {
    // 单行注释 ： 打印输出
    println("hello world")
    /*
    多行注释
    */
    println("这个是多行注释")
  }
}
