package chapter09

import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

/*
* scala基础语法
* 异常处理 Scala 的方法可以通过抛出异常的方法的方式来终止相关代码的运行，不必通过返回值
* throw new IllegalArgumentException
* */
object ExceptionDemo {
  def main(args: Array[String]): Unit = {
    try {
      val f = new FileReader("input.txt")
    } catch {
      case ex: FileNotFoundException => {
        println("Missing file exception")
      }
      case ex: IOException => {
        println("IO Exception")
      }
    } finally { // finally 语句用于执行不管是正常处理还是有异常发生时都需要执行的步骤
      println("Exiting finally...")
    }
  }
}
