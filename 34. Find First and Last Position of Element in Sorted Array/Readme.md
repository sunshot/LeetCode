# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array.
- -10^9 <= target <= 10^9

Solution1: To achieve O(log n) runtime complexity, we need to use binary search. if nums[mid] greater or less than target, we know the change condition. But what action if nums[mid] = target? We need to change left and right directly. Runtime: 84 ms, faster than 72.15% of Python3 online submissions for Find First and Last Position of Element in Sorted Array. But in worst case, for example, when all the elements are the same as target, then time complexity is O(n)

Solution2: Use two binary search to find the leftmost and rightmost of the target value in the list. Runtime: 84 ms, faster than 72.15% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.


