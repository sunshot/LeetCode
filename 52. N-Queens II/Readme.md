# [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Examples:

```
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Input: n = 1
Output: 1
```

Constraints:

- 1 <= n <= 9

Solution1: Backtracking. 难点在于如何判断对角线不合法，目前通过 ``abs(i - row) == abs(j - col)``进行的判断

See https://leetcode.com/explore/featured/card/recursion-ii/472/backtracking/2804/


Solution2: https://leetcode.com/problems/n-queens-ii/discuss/126533/Python-Backtracking-Solution-(Beats-97)
采用 row+col 及 row-col 来进行判断，如果两个 Queen 在对角线上，则 row+col 或 row-col 必然相等，这样能节省不少时间：Runtime: 48 ms, faster than 84.47% of Python3 online submissions for N-Queens II.
