# [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

Constraints:

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums is guaranteed to be rotated at some pivot.
- -10^4 <= target <= 10^4

Follow up: This problem is the same as Search in Rotated Sorted Array, where nums may contain duplicates. Would this affect the runtime complexity? How and why?

Solution1: 区别是特殊情况难以找到最小的元素，如 mid 跟 right 的元素值相同的情况下，其余同 Search in Rotated Sorted Array

Runtime: 56 ms, faster than 38.26% of Python3 online submissions for Search in Rotated Sorted Array II.


Solution2: Borrow [solution1](https://github.com/sunshot/LeetCode/blob/main/33.%20Search%20in%20Rotated%20Sorted%20Array/solution1.py) but also consider duplicates. See https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/760943

Runtime: 48 ms, faster than 90.46% of Python3 online submissions for Search in Rotated Sorted Array II.
