# [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

Example 1:

```
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
```

Constraints:

- 1 <= nums.length <= 105

- 1 <= nums[i] <= 104

- 1 <= x <= 109

Solution1: Similar to [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) and [github](https://github.com/sunshot/LeetCode/tree/main/209.%20Minimum%20Size%20Subarray%20Sum). We can double nums, and first find the left index, then use the similar method in 209 to the doubled nums. Two pointers sliding window. Runtime: 1272 ms, faster than 34.76% of Python3 online submissions for Minimum Operations to Reduce X to Zero. Need to improve. O(n)


https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935935/Java-Detailed-Explanation-O(N)-Prefix-SumMap-Longest-Target-Sub-Array

If it exists an answer, then it means we have a subarray in the middle of original array whose sum is == totalSum - x
If we want to minimize our operations, then we should maximize the length of the middle subarray.
Then the qeustion becomes: Find the Longest Subarray with Sum Equals to TotalSum - X
We could simply use Map + Prefix Sum to get it!

https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016199/Python-O(n)-solution-using-cumulative-sums

We can reformulate this problem: we need to choose several values from the beginning and several values from end, such that sum of this numbers is equal to x. It is equivalent to finding some contiguous subarray, such that it has sum of elements equal to sum(nums) - x, which has the biggest length. In this way problem becomes quite classical and I prefer to solve it using cumulative sums.

Solution2: find the maximize contiguous subarray with sum equals to sum(nums) - x

Hint 1: Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.

Hint 2: Finding the maximum subarray is standard and can be done greedily.

This problem is somewhat similar to [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) and see in [github](https://github.com/sunshot/LeetCode/tree/main/1695.%20Maximum%20Erasure%20Value)

Other similar problems:

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

- [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)
