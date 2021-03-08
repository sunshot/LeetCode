# 205. Isomorphic Strings

https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

```
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false
```

## Solution

这道题很直接，不过其实有坑。最先想到的是用 itertools.groupby 这样可以快速统计出每个连续字符及其个数，然后用 hash 来判断是否有映射存在。坑在于判断映射时，不能只判断一个方向，比如用一个hash表记录 s 到 t 的映射，如果出现不同的就失败，新出现的就放到hash表里，例子：

```
"badc"
"baba"
```

就会出问题 b->b，d->b，违背了 No two characters may map to the same character，因此需要用两个hash表，记录两个方向的映射

其实不用 itertools.groupby 进行预先统计，直接用两个 hash 表进行判断就行


讨论区参考解答：https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).

## Testcase

```
"egg"
"add"
"foo"
"bar"
"paper"
"title"
"badc"
"baba"
```

相同类似的题：

## 290. Word Pattern

https://leetcode.com/problems/word-pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or not s:
            return False
        words = s.split()
        if len(pattern) != len(words):
            return False
        p2s = {}
        s2p = {}
        for i in range(len(pattern)):
            if pattern[i] in p2s and p2s[pattern[i]] != words[i]:
                return False
            if words[i] in s2p and s2p[words[i]] != pattern[i]:
                return False
            p2s[pattern[i]] = words[i]
            s2p[words[i]] = pattern[i]
        return True
        
```