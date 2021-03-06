# 503. Next Greater Element II

https://leetcode.com/problems/next-greater-element-ii/

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

```
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
```

## Solution

跟 https://leetcode.com/problems/next-greater-element-i 相比，这道题还是不一样，首先 List 中元素不唯一，不能用 dict 来存结果，其次，可以循环去找

解法一：循环找其实相当于把两个List加起来，栈中可以直接存储元素和其位置信息，这样得到 next greater element 后直接写入 ans list中

解法二：只存储位置信息

参考解答：https://leetcode.com/problems/next-greater-element-ii/solution/

用栈但是从右边开始遍历数组，栈内保存的时候可能的 next greater element