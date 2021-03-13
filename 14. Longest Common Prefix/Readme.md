# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

最长前缀，最直接的办法是对每个字符串的起始位置开始判断，看此位置与其他字符串上的字符是否相同，一旦不同，立即返回

参考答案给出了其他不同的解法：https://leetcode.com/problems/longest-common-prefix/solution/