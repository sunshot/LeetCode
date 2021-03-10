# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings s and t , write a function to determine if t is an anagram of s.

```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution

This problem is straightforward, we can sort s and t and compare. Or we can use hash.

Note, using python, we can compare two dicts directly, see https://stackoverflow.com/questions/1911273/is-there-a-better-way-to-compare-dictionary-values/5635309#5635309

Then we can simply:

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = collections.Counter(s)
        t_hash = collections.Counter(t)
        
        return s_hash == t_hash
```

collections.Counter is subclass of dict

This method seems running fastest.

Similar problems:
https://github.com/sunshot/LeetCode/tree/main/242.%20Valid%20Anagram
https://github.com/sunshot/LeetCode/tree/main/438.%20Find%20All%20Anagrams%20in%20a%20String
https://github.com/sunshot/LeetCode/tree/main/567.%20Permutation%20in%20String
