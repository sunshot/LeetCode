# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

与 [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) 有点类似，但更简单，采用滑动窗口和 Python Counter进行比较

Similar problems:
https://github.com/sunshot/LeetCode/tree/main/242.%20Valid%20Anagram
https://github.com/sunshot/LeetCode/tree/main/438.%20Find%20All%20Anagrams%20in%20a%20String
https://github.com/sunshot/LeetCode/tree/main/567.%20Permutation%20in%20String