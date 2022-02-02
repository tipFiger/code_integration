import java.util.Arrays;
import java.util.Scanner;

/*
 *  记录 Java语法习惯：
 *  常量
 *  进制
 *  数据类型
 *  类型转换
 * */
public class JavaBaseSyntax {
    public static void main(String[] args) {
        // A:字符串常量 用""括起来的内容
        System.out.println("HelloWorld");
        // B:整数常量 所有的整数数据
        System.out.println(1);
        // C:小数常量 所有的带小数的数据
        System.out.println(1.5);
        // D:字符常量 用单引号括起来的内容
        System.out.println('A');
        // E:布尔常量 只有两个值：true和false
        System.out.println(true);
        System.out.println(false);

        // 2 8 10 16 进制
        System.out.println(0b100); // 二进制 -》  4
        System.out.println(0100); // 八进制 -》 64
        System.out.println(100); // 十进制
        System.out.println(0x100); // 十六进制 -》 256

        // 基本数据类型：4类八种   引用数据类型：类 接口 数组
        // 整数默认是int类型 浮点数默认是double类型 long类型的变量，要加l或者L。 float类型的变量，要加f或者F。  在同一对{}里面，是不能有同名的变量
        // 数据类型 变量名 = 初始化值;
        // 定义byte类型
        byte i = 15;
        System.out.println(i);
        // 定义short类型
        short a = 15;
        System.out.println(a);
        // 定义int类型
        int b = 15;
        System.out.println(b);
        // 定义long类型
        long c = 15L;
        System.out.println(c);
        // 定义float类型
        float d = 1.5F;
        System.out.println(d);
        // 定义double类型
        double e = 1.5;
        System.out.println(e);
        // 定义char类型
        char f = 'a';
        System.out.println(f);
        // 定义Boolean类型
        boolean g = true;
        System.out.println(g);
        // 没有初始化值不能直接使用
        int h;
        h = 1;
        System.out.println(h);

        // 输入数字
//        Scanner sc = new Scanner(System.in);
//        System.out.println("请输入三个数字：");
//        int[] arr;
//        int aa = 0;
//        arr = new int[3];
//        System.out.println(Arrays.toString(arr));
//        while (true) {
//            arr[i] = sc.nextInt();
//            i++;
//            if (i >= arr.length) {
//                break;
//            }
//        }
//        for (int j = 0; j < arr.length; j++) {
//            System.out.println("arr[" + j + "]=" + arr[j]);
//        }
//
//        int temp = 0;
//        for (int j = 1; j < arr.length; j++) {
//            temp = arr[j - 1] >= arr[j] ? arr[j - 1] : arr[j];
//        }
//        System.out.println("arr数组中最大值为：" + temp);

        // 数组求和
        int[][] arr = {{22,66,44},{77,33,88},{25,45,65},{11,66,99}};
        int sum = 0;
        for (int i1=0; i1<arr.length; i1++) {
            for (int j=0; j<arr[i1].length; j++) {
                sum +=arr[i1][j];
            }
        }
        System.out.println("最终的和：" +sum);

        // 参与运算的数据，要求类型一致。 boolean类型不能转换为其他的数据类型。
        //	隐式转换： A:byte,short,char-->int-->long-->float-->double  B:byte,short,char相互之间不转换，他们参与运算首先转换为int类型
        //类型一样的数据
        int a1 = 10;
        int b1 = 20;
        System.out.println(a1 + b1);
        int c1 = a1 + b1;
        System.out.println(c1);
        System.out.println("--------------");

        //定义变量
        byte by = 3;
        int i11 = 4;
        System.out.println(by + i11);
        int j1 =	by + i11;
        System.out.println(j1);

        // 强制转换:从大到小，不建议使用，因为可能有精度的丢失。 目标类型 变量名=(目标类型)(被转换的数据);
        byte by1 = 3;
        int i2 = 4;
        byte bb = (byte)(by1 + i2);
        System.out.println(bb);























    }
}
