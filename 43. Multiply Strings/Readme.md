# [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/)

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

```
Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
```

Constraints:

- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.

Solution: 

1. compute products from each pair of digits from num1 and num2. 
2. carry each element over. 
3. output the solution.
4. The product of two numbers cannot exceed the sum of the two lengths. (e.g. 99 * 99 cannot be five digit)

https://leetcode.com/problems/multiply-strings/discuss/17608/AC-solution-in-Java-with-explanation

https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
