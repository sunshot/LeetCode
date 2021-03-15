# [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

Similar to [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Solution1: Use hash to keep index: cumulative sum up to index, and includes index. Runtime: 164 ms, faster than 41.43% of Python3 online submissions for Find Pivot Index.

Solution2: Use list to store the info. Runtime: 156 ms, faster than 51.00% of Python3 online submissions for Find Pivot Index.

Solution3: We only need to know toal sum and leftsum, no need to keep cumulative sum. See https://leetcode.com/problems/find-pivot-index/solution/. Runtime: 144 ms, faster than 88.76% of Python3 online submissions for Find Pivot Index.
