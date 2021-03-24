# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

```
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

Input: x = 0
Output: 0
```

Constraints:

- -2^31 <= x <= 2^31 - 1

Solution1: 关键点有两处：一是注意负数，二是注意 overflow，如果不通过将整数转成字符串的方式，可以直接通过求各个位数的方法，边求边乘，同时考虑 overflow

``` java
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```

https://leetcode.com/problems/reverse-integer/solution/


Solution2 and Solution3 都是翻转字符串
