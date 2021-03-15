# [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

Constraints:

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Hint 1:

Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.

Solution1: Based on hint 1. Runtime: 20 ms, faster than 99.22% of Python3 online submissions for House Robber II.

Follow up of [198. House Robber](https://leetcode.com/problems/house-robber/) see in [github](https://github.com/sunshot/LeetCode/tree/main/198.%20House%20Robber)


https://leetcode.com/problems/house-robber-ii/discuss/299071/Python-O(n)-time-O(1)-space
