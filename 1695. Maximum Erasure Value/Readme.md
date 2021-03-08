# [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

```
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
```

This is similar to [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), see the solution in https://github.com/sunshot/LeetCode/tree/main/3.%20Longest%20Substring%20Without%20Repeating%20Characters

https://leetcode.com/problems/maximum-erasure-value/discuss/978849/Python-O(N)-solution-6-lines-use-dictionary

讨论区有个参考解答，对如何求子连续数组的和有优化。sumDic[i] 为 nums[0..i] 的和，这样可以快速求得任意 start...i 的子数组的和: sumDic[i] - sumDic[start-1]

solution2.py 再 solution1.py 基础上进行了优化，不过提交总是 Time Limit Exceeded
