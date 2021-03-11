# [18. 4Sum](https://leetcode.com/problems/4sum/)

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

Similar to: [15. 3Sum](https://leetcode.com/problems/3sum/)

See [github](https://github.com/sunshot/LeetCode/tree/main/15.%203Sum)

与 3Sum 类似，但要注意优化，提前退出条件，优化后可以达到:

Runtime: 80 ms, faster than 97.85% of Python3 online submissions for 4Sum.


参考解答，给出了 kSum 的解法 https://leetcode.com/problems/4sum/solution/
