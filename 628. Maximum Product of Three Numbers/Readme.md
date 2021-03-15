# [628. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

```
Input: nums = [1,2,3,4]
Output: 24

Input: nums = [-1,-2,-3]
Output: -6
```

Constraints:

- 3 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000

Solution1: sort the nums, then we only have the following cases:

- product is positive, then ``nums[-1] * nums[-2] * nums[-3]`` or ``nums[0] * nums[1] * nums[-1]``
- product is negative, then ``nums[-1] * nums[-2] * nums[-3]``

Runtime: 256 ms, faster than 58.93% of Python3 online submissions for Maximum Product of Three Numbers.


Solution2: No sort, just find max1, max2, max3 and min1, min2.

see https://leetcode.com/problems/maximum-product-of-three-numbers/solution/
