# [1. Two Sum](https://leetcode.com/problems/two-sum/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

经典问题，可以暴力搜索，如果不排序，可以使用 hash 记录遍历过的元素；如果排序，则可以使用双指针的方式进行遍历，但本题需要返回元素的 index，所以排序不合适

solution2 利用了 python 的特性，可以根据 val 从 List 寻找 index，实质跟 hash 类似，但时间复杂度高 O(n^2)，不过实际提交运行还挺快
