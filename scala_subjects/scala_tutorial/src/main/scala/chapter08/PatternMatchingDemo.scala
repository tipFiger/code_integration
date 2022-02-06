package chapter08

/*
* scala基础语法
* 模式匹配
* 一个模式匹配包含了一系列备选项，每个都开始于关键字 case。每个备选项都包含了一个模式及一到多个表达式。箭头符号 => 隔开了模式和表达式。
* */
object PatternMatchingDemo {
  def main(args: Array[String]): Unit = {
    println(matchTest1(3))

    val alice = new Person("Alice", 25)
    val bob = new Person("Bob", 32)
    val charlie = new Person("Charlie", 32)

    for (person <- List(alice, bob, charlie)) {
      person match {
        case Person("Alice", 25) => println("Hi Alice!")
        case Person("Bob", 32) => println("Hi Bob!")
        case Person(name, age) =>
          println("Age: " + age + " year, name: " + name + "?")
      }
    }
  }

  // 模式匹配函数 Mathch的使用
  def matchTest1(x: Int): String = x match {
    case 1 => "one"
    case 2 => "two"
    case _ => "many"
  }

  // 样例类
  case class Person(name: String, age: Int)

}


// 在声明样例类时，下面的过程自动发生了：
//   构造器的每个参数都成为val，除非显式被声明为var，但是并不推荐这么做；
//   在伴生对象中提供了apply方法，所以可以不使用new关键字就可构建对象；
//   提供unapply方法使模式匹配可以工作；
//   生成toString、equals、hashCode和copy方法，除非显示给出这些方法的定义。
