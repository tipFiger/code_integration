/*
 * Java基础语法：
 * 形参改变
 * */
public class ArgsDemo {
    public static void main(String[] args) {
        // 基本类型：形式参数的改变对实际参数没有影响。  不可变
        // 引用类型：形式参数的改变直接影响实际参数。    可变
        int a = 10;
        int b = 20;
        System.out.println("a:" + a + ",b:" + b); //a:10,b:20
        change(a, b);
        System.out.println("a:" + a + ",b:" + b); //a:?,b:?

        int[] arr = {1, 2, 3, 4, 5};
        change(arr);
        System.out.println(arr[1]); //?
    }

    public static void change(int a, int b)  //a=10,b=20
    {
        System.out.println("a:" + a + ",b:" + b); //a:10,b:20
        a = b; //a=20;
        b = a + b; //b=40;
        System.out.println("a:" + a + ",b:" + b); //a:20,b:40
    }

    public static void change(int[] arr) //arr = {1,2,3,4,5}
    {
        for (int x = 0; x < arr.length; x++) {
            //如果是偶数，数据变为以前的2倍。
            if (arr[x] % 2 == 0) {
                arr[x] *= 2;
            }
        }

        //{1,4,3,8,5}
    }

}

