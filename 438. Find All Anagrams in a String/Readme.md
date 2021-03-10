# [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```

与 [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) 有点类似，可以采用滑动窗口和dicts(Counter)进行比较的方式来判断

Similar problems:
https://github.com/sunshot/LeetCode/tree/main/242.%20Valid%20Anagram
https://github.com/sunshot/LeetCode/tree/main/438.%20Find%20All%20Anagrams%20in%20a%20String
https://github.com/sunshot/LeetCode/tree/main/567.%20Permutation%20in%20String