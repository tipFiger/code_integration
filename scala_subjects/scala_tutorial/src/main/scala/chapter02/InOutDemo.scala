package chapter02

import java.io.{File, PrintWriter}
import scala.io.{Source, StdIn}

/*
* Scala基础语法：
* 字符串的输出 println
* 键盘输入 StdIn类
* */
object InOutDemo {
  def main(args: Array[String]): Unit = {
    // 字符串 通过+号连接
    val name = "a" + "b"
    val age = 18
    println(age + "的" + name + "在学习")
    // *号 赋值字符串
    println(name * 3)

    // 字符串格式化输出 printf %传值 printf不会自动换行用\n换行
    printf("%d岁的%s在学习\n", age, name)

    // 字符串插值 通过$获取变量值
    println(s"${age}岁的${name}在学习")
    println(f"${age}岁的${name}在学习")

    // 小数默认是double
    val num: Double = 2.3456
    // val num1: Float = 2.3f
    println(f"格式化的数：${num}%.2f")
    println(raw"格式化的数：${num}%.2f") // 只填变量， %.2f就也直接显示了

    // 三引号，保持多行字符串的原格式输出
    val sql =
      s"""
         |select *
         | from table_name
         |where name = ${name}
         |""".stripMargin
    println(sql)

    // 输入：
    // println("请输入姓名：")
    // val name1: String = StdIn.readLine()
    println("请输入年龄：")
    // val age1: Int = StdIn.readInt()
    // println(s"${age1}岁的${name1}来内卷啊")

    // 文件读取数据 Source scala.io 注意路径的斜杠
    // 绝对路径（idea中右键copy path） E:\code_integration\scala_subjects\scala_tutorial\src\main\resources\inouttest.txt
    // 相对路径 src\main\resources\inouttest.txt
    Source.fromFile("src/main/resources/inouttest.txt").foreach(print)

    // 数据写入 入参直接是双引号写路径
    val writer = new PrintWriter(new File("src/main/resources/outtest.txt"))
    writer.write("fine thank you")
    writer.close()
  }
}
