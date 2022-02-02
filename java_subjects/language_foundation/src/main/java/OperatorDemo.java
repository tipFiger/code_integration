/*
 *  记录 Java语法习惯：
 *  算术运算符
 *	赋值运算符
 *	比较运算符
 *	逻辑运算符
 *	位运算符
 *	三目运算符
 * */
public class OperatorDemo {
    public static void main(String[] args) {
        // 算数运算符 +，-，*，/，%，++，--
        System.out.println(10 + 20);
        System.out.println(10 - 20);
        System.out.println(10 * 20);
        //整数相除，只能得到整数
        System.out.println(10 / 20);
        //要想得到小数，可以乘以或者除以1.0
        System.out.println(10 / 1.0 / 20);
        //加法的用法:正号,加法,字符串连接符
        System.out.println(+5);
        System.out.println(1 + 2);
        System.out.println("1" + "2");
        //%和/的区别，一个是余数，一个是商
        System.out.println(5 / 3);
        System.out.println(5 % 3);
        //问题：判断数据整出，用哪个符号。
        //用%,如果余数为0，说明整除。
        System.out.println(5 % 3); //2
        System.out.println(5 % -3);//2
        System.out.println(-5 % 3);//-2
        System.out.println(-5 % 3);//-2
        // ++,--：自增自减运算符。
        int a = 10;
        int b = a++;
        System.out.println(a);//11
        System.out.println(b);//10
        System.out.println("------------");
        int c = 10;
        int d = ++c;
        System.out.println(c);//11
        System.out.println(d);//11
        System.out.println("------------");
        int e = 10;
        //e++;
        ++e;
        System.out.println(e);

        // 赋值运算符： 基本：=  复合：+=,-=,*=,/=,%=,...
        //把10赋值给int类型的变量a
        int a1 = 10;
        //复合的用法
        int b1 = 10;
        b1 += 20; //结果等价于：b = b + 20;
        System.out.println(b1);

        // 关系运算符： ==,!=,>,>=,<,<=
        // 特点： 无论表达式是简单还是复杂，结果肯定是boolean类型。
        // 注意事项： 关系运算符“==”不能误写成“=” 。
        int a2 = 10;
        int b2 = 10;
        int c2 = 20;
        System.out.println(a2 == b2);
        System.out.println(a2 == c2);
        System.out.println((a2 + b2 * c2) == (a2 * b2 + c2));
        System.out.println("----------------");
        System.out.println(a2 = b2); //把b的值赋值给a，把a的值作为结果留下来
        System.out.println(a2 = c2);
        // &&和&的区别? 前者有短路效果，只要左边是false，右边不执行。而后者，全部执行。 ||和|的区别? 前者有短路效果，只要左边是true，右边不执行。而后者，全部执行。
        int a3 = 10;
        int b3 = 20;
        int c3 = 30;
        //&:逻辑与	有false则false
        System.out.println(a3 > b3 & a3 > c3); //false & false = false
        System.out.println(a3 > b3 & a3 < c3); //false & true = false
        System.out.println(a3 < b3 & a3 > c3); //true & false = false
        System.out.println(a3 < b3 & a3 < c3); //true & true = true
        System.out.println("--------");
        //&&:
        System.out.println(a3 > b3 && a3 > c3); //false && false = false
        System.out.println(a3 > b3 && a3 < c3); //false && true = false
        System.out.println(a3 < b3 && a3 > c3); //true && false = false
        System.out.println(a3 < b3 && a3 < c3); //true && true = true
        System.out.println("--------");
        //|:逻辑或	有true则true
        System.out.println(a3 > b3 | a3 > c3); //false | false = false
        System.out.println(a3 > b3 | a3 < c3); //false | true = true
        System.out.println(a3 < b3 | a3 > c3); //true | false = true
        System.out.println(a3 < b3 | a3 < c3); //true | true = true
        System.out.println("--------");
        //||:
        System.out.println(a3 > b3 || a3 > c3); //false || false = false
        System.out.println(a3 > b3 || a3 < c3); //false || true = true
        System.out.println(a3 < b3 || a3 > c3); //true || false = true
        System.out.println(a3 < b3 || a3 < c3); //true || true = true
        System.out.println("--------");
        int x = 3;
        int y = 4;
        //System.out.println((x++)>3 & (y++)>4); //false & false = false
        //System.out.println(x);//4
        //System.out.println(y);//5
        System.out.println((x++) > 3 && (y++) > 4);
        System.out.println(x);//4
        System.out.println(y);//4

        // 逻辑运算符： &,|,!,^ &&,||
        //	注意： 逻辑运算符连接的应该是一个布尔表达式。
        //&,|,!,^
        int a4 = 10;
        int b4 = 20;
        int c4 = 30;

        //&:逻辑与	有false则false
        System.out.println(a4 > b4 & a4 > c4); //false & false = false
        System.out.println(a4 > b4 & a4 < c4); //false & true = false
        System.out.println(a4 < b4 & a4 > c4); //true & false = false
        System.out.println(a4 < b4 & a4 < c4); //true & true = true
        System.out.println("--------");
        //|:逻辑或	有true则true
        System.out.println(a4 > b4 | a4 > c4); //false | false = false
        System.out.println(a4 > b4 | a4 < c4); //false | true = true
        System.out.println(a4 < b4 | a4 > c4); //true | false = true
        System.out.println(a4 < b4 | a4 < c4); //true | true = true
        System.out.println("--------");
        //^:逻辑异或 相同false，不同true。
        //情侣：男男，男女，女男，女女
        System.out.println(a4 > b4 ^ a4 > c4); //false ^ false = false
        System.out.println(a4 > b4 ^ a4 < c4); //false ^ true = true
        System.out.println(a4 < b4 ^ a4 > c4); //true ^ false = true
        System.out.println(a4 < b4 ^ a4 < c4); //true ^ true = false
        System.out.println("--------");
        //!:逻辑非
        System.out.println((a4 > b4));//false
        System.out.println(!(a4 > b4));//true
        System.out.println(!!(a4 > b4));//false
        System.out.println(!!!(a4 > b4));//true
        System.out.println(!!!!(a4 > b4));//false

        // 位运算符：位运算符一定是先把数据转成二进制，然后再运算。
        System.out.println(3 & 4); //0
        System.out.println(3 | 4); //7
        System.out.println(3 ^ 4); //7
        System.out.println(~3); //

        // <<:左移，右边补0  >>:右移，根据最高位确定补齐是0还是1  >>>:无符号右移 左边补0
        System.out.println(4 << 2); //16 = 4 * 2^2
        System.out.println(3 << 3); //3 * 2 ^ 3
        System.out.println(32 >> 2); //32 / 2^2
        System.out.println(32 >>> 2);
        System.out.println(-32 >> 2);
        System.out.println(-32 >>> 2);

        // 三元运算符： (关系表达式)?表达式1：表达式2； 计算关系表达式，看其返回值 true:表达式1就是整个表达式的值 false:表达式2就是整个表达式的值
        //获取两个数据中的较大值
        int x1 = 3;
        int y1 = 4;
        int z1 = (x1 > y1) ? x1 : y1;
        System.out.println(z1);
        //比较两个数是否相等
        int a5 = 4;
        int b5 = 4;
        //boolean flag = (a==b)?true:false;
        boolean flag = (a5 == b5);
        System.out.println(flag);
        //获取三个数据中的较大值
        int c5 = 30;
        int d5 = 40;
        int e5 = 50;
        //int max = (c>d)?(c>e?c:e):(d>e?d:e);
        int temp = (c5 > d5) ? c5 : d5;
        int max = (temp > e5) ? temp : e5;
        System.out.println(max);


    }
}
