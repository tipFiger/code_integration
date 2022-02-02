/*
* java基础语法
* 形参
* */
//定义学生类，写一个love方法
class Student  {
    public void love() {
        System.out.println("学生喜欢放假");
    }
}

class StudentDemo {
    public void test(Student s) {
        s.love();
    }
}

//测试类
class FormalParameter {
    public static void main(String[] args) {
		/*
		//创建对象
		Student s = new Student();
		s.love();
		s.love();
		//匿名对象
		new Student().love();
		new Student().love();
		*/

        //有名字的情况
        //StudentDemo sd = new StudentDemo();
        //Student s = new Student();
        //sd.test(s);

        //没有名字的情况
        //StudentDemo sd = new StudentDemo();
        //sd.test(new Student());

        //不妨在来一步
        new StudentDemo().test(new Student());

        // 封装 private:
        // A:是一个权限修饰符。
        // B:可以修饰成员(成员变量和成员方法)
        // C:被private修饰的成员只在本类中才能访问。

        // this关键字 代表本类的对象

        // static 表示成员变量是被共享的
        // public:访问权限修饰符，表示最大的访问权限，被jvm调用，所有权限要够大。
        // static:被jvm调用，不用创建对象，直接类名访问
        // void:被jvm调用，不需要给jvm返回值
        // main:一个通用的名称，虽然不是关键字，但是被jvm识别
        // String[] args: 早期出现是为了接收键盘录入数据的。


    }
}
