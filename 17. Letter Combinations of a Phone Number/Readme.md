# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Examples:

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
```

Constraints:

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Solution1: 递归，如果知道了 digits[0..n-2] (n = len(digits)) 的字母组合，如何求 digits[0..n-1]？只需要将求得的字母组合与 digits[n-1] 对应的字母再组合在一起即可，因此，可以很直接使用递归来实现。Runtime: 24 ms, faster than 96.34% of Python3 online submissions for Letter Combinations of a Phone Number.


Solution2: Backtracking, see https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/

Use a backtracking function to generate all possible combinations.

- The function should take 2 primary inputs: the current combination of letters we have, path, and the index we are currently checking.
- As a base case, if our current combination of letters is the same length as the input - digits, that means we have a complete combination. Therefore, add it to our answer, and backtrack.
- Otherwise, get all the letters that correspond with the current digit we are looking at, digits[index].
- Loop through these letters. For each letter, add the letter to our current path, and call backtrack again, but move on to the next digit by incrementing index by 1.
- Make sure to remove the letter from path once finished with it.

See [backtracking explore card](https://leetcode.com/explore/featured/card/recursion-ii/472/backtracking/)

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

不过我觉得 Solution1 更容易想到，更好理解，效率也不错

Similar Problems:
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [401. Binary Watch](https://leetcode.com/problems/binary-watch/)
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
