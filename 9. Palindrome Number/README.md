## Solution

就是看数字是不是对称的，最简单的方法就是转成 string，然后 reverse string，判断新旧 string 是否相等，知识点，python 中如何 reverse string？

https://www.w3schools.com/python/python_howto_reverse_string.asp

There is no built-in function to reverse a String in Python.
The fastest (and easiest?) way is to use a slice that steps backwards, -1.

``x_rev = x_str[::-1]``

如果不能转换成 string， 则需要直接把数字进行 reverse，方法就是求出个位数、十位数、、、然后加起来，直接做的话 Java 里面需要判断 是否 overflow

````
int num = x;
        int result = 0;
        while(num>0){
            if(result > Integer.MAX_VALUE / 10 || 
               (result == Integer.MAX_VALUE / 10 && num % 10 > Integer.MAX_VALUE % 10)){
                return false;
            }
            result = result * 10 + num % 10;
            num = num / 10;
        }
````

参考答案很巧妙，其实 reverse 数字不需要彻底做完，只需要做一半，就保证 reversedNumber 大于等于原始的数字即可

````
int result = 0;
        while(x > result){
            result = result * 10 + x % 10;
            x = x / 10;
        }
        return x == result || x == result/10;
````

当数字时奇数位数时，其实不关心中间的数字是啥，直接除以10去掉
