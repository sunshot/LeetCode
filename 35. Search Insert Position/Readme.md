# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

```
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 0
Output: 0

Input: nums = [1], target = 0
Output: 0
```

Constraints:

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4

Solution1: target may not in the list, need to take care when scanning the list.
Runtime: 48 ms, faster than 73.73% of Python3 online submissions for Search Insert Position.

Solution2: https://leetcode.com/problems/search-insert-position/discuss/15081/Python-one-liner-48ms


Solution3: Binary Search
