# [15. 3Sum](https://leetcode.com/problems/3sum/)

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

This is followup of [1. Two Sum](https://leetcode.com/problems/two-sum/) see [github](https://github.com/sunshot/LeetCode/tree/main/1.%20Two%20Sum)

题目要求输出符合条件的三元组，并且不能重复，因为没有序号的问题，直接排序后容易解决

solution1：排序后对每一个元素，判断当前位置之后否存在符合条件的 two sum 存在，利用 two pointers的思路求解，需要注意的是，要考虑重复元素

solution2：在1的基础上稍微改进，能从 1100ms+ 缩减为 600ms。改进有：如果 nums[i] 已经大于0了，立即退出。另外，在求解 two sum 时，删除不需要的循环，提高效率，只有当找到符合条件的 two sum时，左右指针一侧考虑重复，往后循环即可


