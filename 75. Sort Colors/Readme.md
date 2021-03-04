# 75. Sort Colors

https://leetcode.com/problems/sort-colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

## Solution

最直接的方式当然是直接调用 sort 方法，考虑到 List 元素只有 0 1 2 可以分别统计他们的个数，然后重新改写 List


讨论区精彩的解法：


https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation

用了三个 pointer，很巧妙