# [90. Subsets II](https://leetcode.com/problems/subsets-ii/)

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]
```

Constraints:

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

This problem is similar to [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/). We can solve the duplicates by sorting or Counter. See [in github](https://github.com/sunshot/LeetCode/tree/main/40.%20Combination%20Sum%20II).

Solution1. Sorting and then Backtracking. Runtime: 36 ms, faster than 78.55% of Python3 online submissions for Subsets II.

Solution2. Counter and then Backtracking. Runtime: 36 ms, faster than 78.55% of Python3 online submissions for Subsets II.
