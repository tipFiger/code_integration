/*
 * java基本语法习惯：
 * 定义方法
 *
 *
 *
 *
 *
 *
 *
 * */

public class MethodDemo {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        // 调用函数
        int result = sum(1, 2);
        System.out.println(result);
        // 调用无返回值函数
        getNum(1);
        // 调用重写函数
        System.out.println(sum(1.2, 2));


    }

    // 定义方法
    //  修饰符 返回值类型 方法名(参数类型 参数名1，参数类型 参数名2…) {
    //      方法体;
    //      return 返回值;
    //  }
    // 有返回值
    public static int sum(int a, int b) {
        int c = a + b;
        return c;
    }

    // 没有明确返回值用void
    public static void getNum(int d) {
        System.out.println("*");
    }

    // 方法重载，同名不同参即可
    public static double sum(double a, double b) {
        double c = a + b;
        return c;
    }

}
