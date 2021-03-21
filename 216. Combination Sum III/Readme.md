# [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

```
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.
```

Constraints:

- 2 <= k <= 9
- 1 <= n <= 60

Solution1: Backtracking. 选择：[1..9]，成功条件，和等于 n 并且出现了 k 个数字. Runtime: 32 ms, faster than 69.61% of Python3 online submissions for Combination Sum III.

Similar Problems:

- [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
- [89. Gray Code](https://leetcode.com/problems/gray-code/)
- [775. Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/)
- [1146. Snapshot Array](https://leetcode.com/problems/snapshot-array/)