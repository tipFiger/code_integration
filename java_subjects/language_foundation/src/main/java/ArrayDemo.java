/*
 * Java基础语法：
 * 一维数组
 * 二维数组
 *
 * */
public class ArrayDemo {
    public static void main(String[] args) {
        // 数组（容器）：存储同一种数据类型的多个元素的集合 int[] arr; 或者 int arr[];
        // 动态初始化：数据类型[] 数组名 = new 数据类型[数组长度];
        int[] arr1 = new int[3];
        System.out.println(arr1); // 获取地址值
        System.out.println(arr1[0]);
        System.out.println(arr1[1]);
        System.out.println(arr1[2]);
        // 数组元素赋值
        arr1[0] = 10;
        System.out.println(arr1[0]);
        // 静态初始化：数据类型[] 数组名 = new 数据类型[]{元素1,元素2,…};
        int[] arr2 = new int[]{1, 2, 3};
        System.out.println(arr2[0]);
        // 简化静态初始化
        int[] arr3 = {1, 2, 3};
        System.out.println(arr3[0]);
        // 数组越界
        // System.out.println(arr1[3]);
        // 空指针：去除堆内存
        // arr1 = null;
        // System.out.println(arr1[1]);

        // 定义二维数组 int[][] arr = new 数据类型[m][n] m表示有几个一维数组，n表示每个一维数组的元素个数
        int[][] arrs1 = new int[3][2];
        // 输出元素
        System.out.println(arrs1[1][0]);
        // 静态初始化：数据类型[][] 变量名 = new 数据类型[][]{{元素…},{元素…},{元素…}}; 数据类型[][] 变量名 = {{元素…},{元素…},{元素…}};
        int[][] arrs2 = new int[][]{{1, 2}, {2, 3}};
        System.out.println(arrs2[1][1]);
        int[][] arrs3 = {{1, 2}, {2, 3}};
        System.out.println(arrs3[1][1]);

    }
}
