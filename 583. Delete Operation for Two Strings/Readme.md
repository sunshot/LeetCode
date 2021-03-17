# [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

```
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Input: word1 = "leetcode", word2 = "etco"
Output: 4
```

Constraints:

- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.

Similar Problems:

- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)


Solution1: Dynamic Programming. dp[i+1][j+1] indicates the minimum number of steps required to make word1[0..i] and word2[0..j] the same.

```python
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for j in range(len(word2)):
            dp[0][j+1] = j+1
        for i in range(len(word1)):
            dp[i+1][0] = i+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
```

Solution2: We can call [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/), and then can know the minimum number of steps.


Reference solution also uses these methods. https://leetcode.com/problems/delete-operation-for-two-strings/solution/

