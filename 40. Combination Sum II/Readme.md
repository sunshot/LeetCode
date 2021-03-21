# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

```

Constraints:

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

Solution1: 参考 [39. Combination Sum](https://leetcode.com/problems/combination-sum/) 进行修改，让每个元素只出现一次，先把 candidates 进行排序，然后借鉴 [491. Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences/) 思路进行调整，每次新增加第x个元素时，第一次可以立即增加，后序再次增加第x个元素的时候，需要判断 nums[i] == nums[i-1]，提交成功，不过还需要优化：Runtime: 96 ms, faster than 38.64% of Python3 online submissions for Combination Sum II.


Solution2: https://leetcode.com/problems/combination-sum-ii/solution/ 使用 Counter 来记录使用的candidate的数量，然后用于保证只出现一次。Runtime: 60 ms, faster than 69.92% of Python3 online submissions for Combination Sum II.


Similar Problems:

- [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

