# 556. Next Greater Element III

https://leetcode.com/problems/next-greater-element-iii/

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

```
Input: n = 12
Output: 21
```

## Solution

首先将正整数转成 List，然后判断是否存在 next greater element，如果所有元素都不存在，则返回 -1

从最右边开始，找到第一个有 next greater element的元素，比如 i， 从 i+1 到 len(num) 中找到最小的大于 num[i] 的元素，然后将此元素与 i 位置交换，最终的结果是 ``num[0:i+1] + sorted(num[i+1:])``

https://www.geeksforgeeks.org/find-next-greater-number-set-digits/

这里没有找 next greater element，不过基于假设：必须存在某个位置 i-1, num[i] > num[i-1]，否则，答案不存在，这里的参考 code 对于输入试个位数没有处理到，有bug

讨论区这个解答非常好：
https://leetcode.com/problems/next-greater-element-iii/discuss/983076/Python-O(m)-solution-explained


类似的问题：
https://leetcode.com/problems/next-permutation

## Test case

```
12
21
132
218765
1234
4321
534976
1
12222333
```