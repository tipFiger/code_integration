package chapter09

import java.io.{File, PrintWriter}
import scala.io._

/*
* scala基础语法
* 文件I/O
*  Scala 进行文件写操作，直接用的都是 java中 的 I/O 类 （java.io.File)
* */
object FileIODemo {
  def main(args: Array[String]): Unit = {
    // 文件写
    val writer = new PrintWriter(new File("20220207.txt"))

    writer.write("嘻嘻怪")
    writer.close()

    // 文件读
    println("文件内容为:\n")

    Source.fromFile("20220207.txt").foreach {
      print
    }

    // 控制台读取
    print("控制台 : " )
    val line = StdIn.readLine()

    println("谢谢，你输入的是: " + line)

  }
}
