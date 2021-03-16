# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Solution1: Use division and consider integer of nums may be zero.

Solution2: Do not use division. We use left[i] indicates product of 0..i-1 and right[i] indicates product of n-1..i+1. Similar to [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) and [in github](https://github.com/sunshot/LeetCode/tree/main/42.%20Trapping%20Rain%20Water)

Solution3: Use result array to store left and right, so we can achive O(1) extra space.

