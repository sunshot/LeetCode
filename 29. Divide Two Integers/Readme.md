# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, assume that your function returns 2^31 − 1 when the division result overflows.

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Input: dividend = 0, divisor = 1
Output: 0

Input: dividend = 1, divisor = 1
Output: 1
```

Constraints:

- -2^31 <= dividend, divisor <= 2^31 - 1
- divisor != 0

Solution1: 最大的正整数：2^31 - 1 (2147483647, Integer.MAX_VALUE), 最小的负整数：-2^31 (2147483648, Integer.MIN_VALUE)。因此，最直接的方法，就是先判断被除数和除数结果的符号，然后求出它们的绝对值，然后不断的用被除数减去除数。但坑在于需要判断是否 overflow，比如一旦有数时最小负整数，取abs的时候会有问题。 Runtime: 2681 ms, faster than 5.01% of Java online submissions for Divide Two Integers.

Solution2: 

https://leetcode.com/problems/divide-two-integers/discuss/142849/C%2B%2BJavaPython-Should-Not-Use-%22long%22-Int

Runtime: 1 ms, faster than 99.98% of Java online submissions for Divide Two Integers.