# 28. Implement strStr()

https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

```python
n = len(haystack)
m = len(needle)
```

Java 的 indexOf，python 的 find 的实现

除了最直接的暴力搜索，时间复杂度 O(nm)，最经典的算法时 KMP，时间复杂度 O(n+m)

https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

https://www.zhihu.com/question/21923021

