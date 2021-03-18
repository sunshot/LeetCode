# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```

Constraints:

- 1 <= n <= 8

Similar Questions:

- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Solution1:
https://leetcode.com/problems/generate-parentheses/solution/

Closure Number: n 个括号的组合，可以由 n-1 个括号的组合增加一个括号而来，增加括号时，可以把 n-1 个组合拆分成 i 和 n-1-i 个括号的组合

```python
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    ans.append('({}){}'.format(left, right))
```

坑： 最早以为 n 跟 n-1 的组合的差异时：对 n-1 的每一个组合，首尾各增加一个括号，最外层再增加一个括号，这实际上漏掉了很多情况，比如 n = 4 时，有一种组合："(())(())" 无法通过上述方式由 n = 3 变换而来


Solution2:
https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution

The idea here is to only add '(' and ')' that we know will guarantee us a solution (instead of adding 1 too many close). Once we add a '(' we will then discard it and try a ')' which can only close a valid '('. Each of these steps are recursively called.

We miss the point that when the code is out of the backtrack, THE STR IS NOT CHANGED.
For the first time, open < max , than enter the backtrack. In this backtrack, str = '('. But when it is out of this backtrack, str still equals to ‘ ’；
Same as the first backtrack when we enter. at this part, str = '('. Because open < max, we enter the next backtrack, which leads to str = '((‘. But if we drump out of this backtrack, the str IS EQUAL TO '('. Then, because of close < open, we enter into the backtrack that backtrack(list, str+")", open, close+1, max);. In this backtrack, str = ‘(()’.