# 209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

此题与 https://leetcode.com/problems/minimum-window-substring/ 有点相似，可以直接使用滑动窗口的办法进行处理

solution1 就是这样的结果，O(n)

solution2 用了二分查找，详见讨论区参考解答：https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O(n)-and-O(n-log-n)-solution