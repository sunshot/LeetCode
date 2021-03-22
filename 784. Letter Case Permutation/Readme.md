# [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

```
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Input: S = "3z4"
Output: ["3z4","3Z4"]

Input: S = "12345"
Output: ["12345"]

Input: S = "0"
Output: ["0"]
```

Constraints:

- S will be a string with length between 1 and 12.
- S will consist only of letters or digits.


Solution1: Bitmask. 借鉴 [78. Subsets](https://leetcode.com/problems/subsets/) Solution3 的思想，生成一个 bitmask，当 bitmask[j] 为1时，交换 letter case，利用 set 来去重。效率很低：Runtime: 120 ms, faster than 11.22% of Python3 online submissions for Letter Case Permutation.

Solution2: Backtracking. Runtime: 872 ms, faster than 7.28% of Python3 online submissions for Letter Case Permutation.

Solution3: Backtracking. Improve Solution2. Runtime: 52 ms, faster than 88.03% of Python3 online submissions for Letter Case Permutation. Solution2 中 Backtrack 没有必要利用循环，直接判断当前 index 即可
