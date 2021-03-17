# [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

Constraints:

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Hints:

- Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
- DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise

Similar Problems:

- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) and [github](https://github.com/sunshot/LeetCode/tree/main/516.%20Longest%20Palindromic%20Subsequence)
- [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
- [1092. Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)



Solution1:


https://www.youtube.com/watch?v=Qf5R-uYQRPk

https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis

动态规划才有可能比较容易求解，尤其是要求时间复杂度的情况下。

令 dp[i+1][j+1] 表示 text1[0..i] 和 text2[0..j] 的 longest common subsequence 的长度，dp[0][0] = 0, 则有:

```python
if text1[i] == text2[j]:
    dp[i+1][j+1] = dp[i][j] + 1
else:
    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
```

