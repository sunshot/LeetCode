# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

Given an unsorted integer array nums, find the smallest missing positive integer.

```
Input: nums = [1,2,0]
Output: 3

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [7,8,9,11,12]
Output: 1
```

Constraints:

- 0 <= nums.length <= 300
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

Solution1: Sort

Solution2: Bitmask. Bitmask 有时候可以当作hash或者set使用，降低空间复杂度
