# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Constraints:

- 1 <= n <= 45

Solution1: Dynamic Programming. dp[i] is total ways to reach i steps. Then dp[i] = dp[i-1] + dp[i-2]