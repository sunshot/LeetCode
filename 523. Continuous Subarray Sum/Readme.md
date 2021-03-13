# [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

```
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
```

This problem is similar to [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) and [1. Two Sum](https://leetcode.com/problems/two-sum/)

可以采用类似的方法，即对每个位置i，判断以i为终点的数组，是否有连续的和是 k 的整数倍

坑：

- k 可以是 0 或者负数，为0的时候需要单独考虑，为负数直接变成正数即可

- k 的整数倍，这里的 n 可以是正整数、0、负整数，尤其是要考虑 n = 0，即只要有连续子数组和为0，基本都能满足 k 的 n 倍

- 连续子数字要求至少两个元素，这个跟 [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) 是不一样的，因此判断i的时候，i-1的累积和（0..i-1 包括 i-1）是不能放到hash/set中，此时只能放入 i-2 的累积和

- 上一个坑的后续，当 i>0时，如何判断 0..i 的累积和满足要求？需要增加一个 0 的累积和到 hash/set中，即需要考虑 nums 为2时的情况

- n 倍可能时很大的数，需要考虑效率，即遍历 n 还是遍历已经放入 hash/set 中的累积和？

惨痛教训：submit 7 次才成功被接受：Runtime: 208 ms, faster than 83.37% of Python3 online submissions for Continuous Subarray Sum.

讨论区解答：
https://leetcode.com/problems/continuous-subarray-sum/discuss/99503/Need-to-pay-attention-to-a-lot-of-corner-cases...

hash 中可以存储 currSum % k 的结果，只有前面的累积和也有相同的 mod 的结果，才表示有连续的子数组，和是k的n倍，为了满足子数组至少2个元素的要求，hash的值可以是mode第一次出现的index，另外 k=0 需要单独考虑，即需要判断 nums 是否有连续的两个 0

## Test case

```
[23,2,4,6,7]
6
[23,2,6,4,7]
6
[23,2,6,4,7]
5
[23,2,4,6,7]
-6
[23,2,6,4,7]
0
[0,1,0]
0
[0,0]
0
[1,2]
3
[23,2,4,6,7]
25
[23,2,4,6,7]
23
[0,0]
-1
[1,1000000000]
1
[1,1000000000]
2
```