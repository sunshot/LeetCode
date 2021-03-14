# [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

Solution1: two pointers solution. We maintain left and right two pointers, for each right, left..right product < k or we can not find the possible left (left will be right+1). Runtime: 1112 ms, faster than 56.45% of Python3 online submissions for Subarray Product Less Than K. Need to improve.

Corner case: 

```
[1,1,1]
1
```

Solution2 is some improvements based on Solution1. Runtime: 1084 ms, faster than 75.65% of Python3 online submissions for Subarray Product Less Than K.


Reference solution: https://leetcode.com/problems/subarray-product-less-than-k/solution/ transfers this problem to Subarray Sum Less Than logK, very smart.


