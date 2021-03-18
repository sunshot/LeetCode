# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
1. Open brackets must be closed in the correct order.

Examples:

```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

Constraints:

- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.


Solution1: 考虑到有三种不同的左括号，直接计数判断会有问题，如："([)]", "[{]"，所以采用栈的方式进行配对. Runtime: 24 ms, faster than 95.79% of Python3 online submissions for Valid Parentheses.
