# [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```

Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100

Solution1: Dynamic Programming. row 0 and col 0 should be computed directly from (0, 0). for any (i, j), dp[i][j] = min(d[i-1][j], d[i][j-1]) + grid[i][j]

See discussion: https://leetcode.com/problems/minimum-path-sum/discuss/23471/DP-with-O(N*N)-space-complexity
