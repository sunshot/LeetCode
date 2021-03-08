# [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

```
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

讨论区解答：

https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution

You will be considering substrings starting at left and ending at right (inclusive). To do this you will iterate over all lengths from 1 to n and within each length iterate over staring (or left) position. The key is that you get the answers for a single length at all start positions before going to the next length because the dp depends on the answers from shorter lengths. If you do it this way you will have 3 cases to consider on every iteration, pick the one with the highest value.

- the answer from removing the left edge char
- the answer from removing the right edge char
- and if the left and right chars are equal, 2 plus the answer from removing both left and right

the 3rd case is how the answer grows. After iterating through all you will have performed O(n^2) checks and used O(n^2) memory, the answer is where left is 0 and right is n-1 which will be your very last calculation.

https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99129/Python-DP-O(n)-space-O(n2)-time


采用动态规划来解，核心思想：用 dp[i][j] 表示字符串 s[i]..s[j] (包括i和j) 最长 Palindromic 子序列，则：

If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])

实际程序计算 dp 时，需要尽可能让i j之间差值越小开始计算