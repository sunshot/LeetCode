# [78. Subsets](https://leetcode.com/problems/subsets/)

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

Constraints:

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Solution1: Backtracking. See [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) and [39. Combination Sum](https://leetcode.com/problems/combination-sum/). Runtime: 36 ms, faster than 58.03% of Python3 online submissions for Subsets.

https://leetcode.com/problems/subsets/solution/


Solution2: Cascading. Let's start from empty subset in output list. At each step one takes new integer into consideration and generates new subsets from the existing ones. Runtime: 28 ms, faster than 94.36% of Python3 online submissions for Subsets.

Solution3: Lexicographic (Binary Sorted) Subsets. The idea is that we map each subset to a bitmask of length n, where 1 on the ith position in bitmask means the presence of nums[i] in the subset, and 0 means its absence. For instance, the bitmask 0..00 (all zeros) corresponds to an empty subset, and the bitmask 1..11 (all ones) corresponds to the entire input array nums. Runtime: 32 ms, faster than 82.45% of Python3 online submissions for Subsets.

It might seem simple at first glance to generate binary numbers, but the real problem here is how to deal with zero left padding, because one has to generate bitmasks of fixed length, i.e. 001 and not just 1. For that one could use standard bit manipulation trick:

```python
nth_bit = 1 << n
for i in range(2**n):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i | nth_bit)[3:]
```

or keep it simple stupid and shift iteration limits:

```python
for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]
```