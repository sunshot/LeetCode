# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

## Solution

首先要弄清楚题目的意思，找到最长的 substring，这个 substring 里面没有重复的字符。 Substring 的意思就是连续的字字符串

思路：用一个 hash 表记录每个字符出现的位置，从 start = 0 开始寻找 substring，条件是不能有重复的字符串，通过 hash 表来判断，但发现位置 i 的字符已经出现在 hash 表了，则表示 substring 已经结束了，长度为 i-start，下一个符合条件的 substring 需要从位置i的字符上一次出现的位置 hash[s[i]]+1 开始。

此处的难点是，如何处理 hash 表？最直接的方法是，位置 hash[s[i]] 之前的字符都需要从 hash 表中删除，这样复杂度高，其实不需要删除这些字符，只需要增加判断条件：位置 i 的字符出现在 hash 表，并且 hash[s[i]] >= start，则表明位置 i 的字符在当前符合条件的 substring 中重复了

```python
        for i in range(len(s)):
            if s[i] in stringIndex and stringIndex[s[i]] >= start:
                # find repeat string s[i], need to reset start index from previous s[i] + 1
                start = stringIndex[s[i]] + 1
            else:
                result = max(result, i-start+1)
            stringIndex[s[i]] = i 
```

实现上，比较巧妙的是，当位置 i 的字符不符合 substring 的条件时，只更新 start 的位置，否则，更新符合条件的 substring，这样的好处是不用单独考虑最后字符串结束的情况了

