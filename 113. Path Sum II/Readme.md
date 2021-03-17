# [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
```

Constraints:

- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

Similar Problems:

- [112. Path Sum](https://leetcode.com/problems/path-sum/)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

思路：递归的 DFS，需要保存根到叶子节点的 Path
