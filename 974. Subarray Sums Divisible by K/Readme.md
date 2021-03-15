# [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

```
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

Note:

- 1 <= A.length <= 30000
- -10000 <= A[i] <= 10000
- 2 <= K <= 10000

Similar to [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) and [github](https://github.com/sunshot/LeetCode/tree/main/523.%20Continuous%20Subarray%20Sum)


Solution1: Use hash to store the number of cumulative sum % K. Runtime: 288 ms, faster than 91.19% of Python3 online submissions for Subarray Sums Divisible by K.

My solution is also similar to https://leetcode.com/problems/subarray-sums-divisible-by-k/solution/

