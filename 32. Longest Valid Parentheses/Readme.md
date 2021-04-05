# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Input: s = ""
Output: 0

```

Constraints:

- 0 <= s.length <= 3 * 104
- s[i] is '(', or ')'

Test Case:

```
()(()
```

Solution1: 从结尾开始扫描，每次判断包括这个结束的字符串中，最长有效的括号的长度，时间复杂度 O(n^2)

Runtime: 396 ms, faster than 5.67% of Python3 online submissions for Longest Valid Parentheses. Need to improve.

Solution2: Solution1 的基础上优化，其实扫描一遍已经知道了哪些子字符串是合法的括号，因为合法的括号子字符串已经从栈中pop了，因此只需要再判断栈中存在哪些字符（记录它们的index），就可以知道合法的子字符串的长度了，O(n)

Runtime: 44 ms, faster than 71.05% of Python3 online submissions for Longest Valid Parentheses.
