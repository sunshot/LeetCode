# [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Examples:

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []

Input: candidates = [1], target = 1
Output: [[1]]

Input: candidates = [1], target = 2
Output: [[1,1]]
```

Constraints:

- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200
- All elements of candidates are distinct.
- 1 <= target <= 500


Solution1: Backtracking. path 记录当前遍历过的candidates，设定退出条件 sum(path) == target，或者找不到结果：sum(path) > target, len(path) > 150。回溯时为了去重，每次只能从自己的index开始的位置开始添加元素。Runtime: 100 ms, faster than 38.87% of Python3 online submissions for Combination Sum. Memory Usage: 14.5 MB, less than 25.86% of Python3 online submissions for Combination Sum. 效率有待提高。

Solution2: 优化不需要每次计算 path 的和，Runtime: 88 ms, faster than 53.22% of Python3 online submissions for Combination Sum.

https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.

Solution3: 再次优化，不需要保存 path，每次调用的时候生成一个新的 path. Runtime: 84 ms, faster than 60.95% of Python3 online submissions for Combination Sum.


https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

