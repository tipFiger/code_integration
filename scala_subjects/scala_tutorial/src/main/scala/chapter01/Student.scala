package chapter01

class Student(name:String, var age:Int) { // 属性和类似Java的构造方法都写好了
  def printInfo():Unit = {
    println(name + " " + this.age + " " + age + " " + Student.school)
  }
}

// 引入伴生对象
object Student {
  // 声明属性
  val school: String = "xx"

  def main(args: Array[String]): Unit = {
    val alice = new Student("alice", age = 20)
    val bob = new Student("bob", age = 21)

    alice.printInfo()
    bob.printInfo()
  }


}
