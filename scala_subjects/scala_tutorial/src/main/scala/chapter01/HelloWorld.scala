package chapter01

/*
* object:关键字 表示声明一个单例对象（伴生对象）
* def 方法名称(参数名称:参数类型)
*
* */
object HelloWorld {
  /*
  * main方法：从外部可以直接调用执行的方法
  * def  方法名称(参数名称:参数类型):返回值类型 = {方法体}
  * def 是个关键字
  * array Scala的集合类型 []表示泛型   名称和类型和Java反着来
  * unit表示没有返回值
  * */
  def main(args: Array[String]): Unit = {
    println("hello world")
    System.out.println("hello scala")
  }
}
