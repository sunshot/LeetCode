# [62. Unique Paths](https://leetcode.com/problems/unique-paths/)

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

Constraints:

- 1 <= m, n <= 100
- It's guaranteed that the answer will be less than or equal to 2 * 10^9.

Solution1: Dynamic Programming. Similar to [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/). We can know row 0 and col 0 are all just 1 path. Then for any other i, j. dp[i][j] = dp[i-1][j] + dp[i][j-1]

Corner case: 
m = 1
n = 1

https://leetcode.com/problems/unique-paths/discuss/23234/Accpeted-simple-Python-DP-solution.

Similar questions:
- [91. Decode Ways](https://leetcode.com/problems/decode-ways)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

