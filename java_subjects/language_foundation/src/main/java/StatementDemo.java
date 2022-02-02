/*
 *  记录 Java语法习惯：
 *  顺序语句 按顺序执行 理解为面向过程编程
 *  选择语句  if | switch |
 *  循环语句  for | while | do while
 *  控制跳转语句 break | continue | return
 * */

public class StatementDemo {
    public static void main(String[] args) {
        int a = 3;
        if (a == 3) {
            System.out.println("这个数等于3");
        }
        if (a > 5) {
            System.out.println("这个数大于3");
        }
        System.out.println("over");


        int x = 10;
        int y = 20;
        // 关系表达式无论简单还是复杂，结果必须是boolean类型 在做判断的时候，建议常量放左边。
        if (x < y) {
            // if语句控制的语句体如果是一条语句，大括号可以省略； 如果是多条语句，就不能省略。建议永远不要省略
            // 一般来说：有左大括号就没有分号，有分号就没有左大括号
            System.out.println("yes");
        }

        // if else
        if (x > y) {
            System.out.println("no");
        } else {
            System.out.println("yes");
        }

        // 三元运算符能够实现的，if语句的第二种格式都可以实现
        int a1 = 1;
        int b1 = 2;
        int c1 = (a1 > b1) ? a1 : b1;
        System.out.println(c1);
        int d1;
        if (a1 > b1) {
            d1 = a1;
        } else {
            d1 = b1;
        }
        System.out.println(d1);

        // if else if else
        int score = 100;
        if (score < 0 || score > 100) {
            System.out.println("输入的成绩有误");
        } else if (score >= 90 && score <= 100) {
            System.out.println("优秀");
        } else if (score >= 80 && score < 90) {
            System.out.println("好");
        } else if (score >= 70 && score < 80) {
            System.out.println("良");
        } else if (score >= 60 && score < 70) {
            System.out.println("及格");
        } else {
            System.out.println("不及格");
        }

        // switch语句
        // A:case后面只能是常量，不能是变量，而且，多个case后面的值不能出现相同的
        // B:default可以省略吗
        // 可以省略。一般不建议。除非判断的值是固定的。
        // C:break可以省略吗
        // 可以。最后一个肯定是没有任何问题的。
        // 中间的省略也是可以的，但是不建议，因为可能对我们想要的结果产生影响。
        // D:default的位置一定要在最后吗
        // 不一定，可以在任何和case相对应的位置。
        // 但是，这个时候，最好加上break。
        // E:switch语句的结束条件
        // a:遇到break。
        // b:执行到程序的末尾
        int week = 4;
        switch (week) {
            case 1:
                System.out.println("星期一");
                break;
            case 2:
                System.out.println("星期二");
                break;
            case 3:
                System.out.println("星期三");
                break;
            case 4:
                System.out.println("星期四");
                break;
            case 5:
                System.out.println("星期五");
                break;
            case 6:
                System.out.println("星期六");
                break;
            case 7:
                System.out.println("星期日");
                break;
            default:
                System.out.println("你输入的数据有误");
                break;
        }

        //循环语句： 初始化:做一些初始操作 条件判断:让我们知道要做多少次 循环体:就是要做的事情 控制条件变化:通过控制条件，让我们在合适的时候结束
        // for循环的格式：
        //    for(初始化语句;判断条件语句;控制条件语句) {
        // 	          循环体语句;
        //    }
        // 执行流程： 首先执行初始化语句 其次执行判断条件语句，看其返回值
        //  执行循环体语句 执行控制条件语句 继续判断
        for (int x1 = 1; x < 10; x++) {
            System.out.println("yes");
        }

        // 求数的阶乘
        int jc = 1;
        for (int ch = 1; ch < 5; ch++) {
            jc *= ch;
        }
        System.out.println("5的阶乘：" + jc);

        // 统计水仙花数
        int count = 0;
        for (int sx = 100; sx < 1000; sx++) {
            int ge = sx % 10;
            int shi = sx / 10 % 10;
            int bai = sx / 10 / 10 % 10;

            if (sx == (ge * ge * ge + shi * shi * shi + bai * bai * bai)) {
                System.out.println(sx); // 具体的数
                count++;
            }
        }
        System.out.println("水仙花总数：" + count); // 显示总个数

        // while循环
        // while (条件表达式) {
        //     语句体;
        // }
        int sxw = 100;
        int cnt = 0;
        while (sxw < 1000) {
            int ge = sxw % 10;
            int shi = sxw / 10 % 10;
            int bai = sxw / 10 / 10 % 10;
            if (sxw == (ge * ge * ge + shi * shi * shi + bai * bai * bai)) {
                System.out.println(sxw);
                cnt++;
            }
            sxw++;
        }
        System.out.println("水仙花总数：" + cnt);

        // for循环结束，该变量就从内存中消失，能够提高内存的使用效率

        // do {
        //     语句体;
        // }while(条件表达式);
        int sum = 0;
        int xd = 1;
        do {
            sum += xd;
            xd++;
        } while (xd <= 100);
        System.out.println(sum);

        // 嵌套循环
        for(int yy=0; yy<4; yy++) {
            for(int xx=0; xx<5; xx++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // break的使用
        for(int xb1=0; xb1<10; xb1++) {
            //System.out.println(x);
            if(xb1%2==0) {
                break;
                //break后面是不能有东西的
                //System.out.println(x);
            }

            System.out.println(xb1);
        }
        System.out.println("-------------");

        wc:for(int xb2=0; xb2<3; xb2++) {
            nc:for(int yb2=0; yb2<4; yb2++) {
                System.out.print("*");
                break;
            }
            System.out.println();
        }

        // continue
        for(int xc1=0; xc1<10; xc1++) {
            if(xc1%2==0) {
                //break;  //结束当前循环
                continue; //结束本次循环操作，进入下一次操作
            }
            System.out.println(xc1);
        }

        wc:for(int xc2=0; xc2<3; xc2++) {
            nc:for(int yc2=0; yc2<4; yc2++) {
                System.out.print("*");
                continue wc;
            }
            System.out.println();
        }

        // return
        for(int xr1=0; xr1<10; xr1++) {
            if(xr1%3==0) {
                //break;
                //continue;
                return;
            }
            System.out.println(xr1);
        }

        System.out.println("over");


    }
}
