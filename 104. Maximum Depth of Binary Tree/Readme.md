# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Input: root = []
Output: 0

Input: root = [0]
Output: 1
```

Constraints:

- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

Solution1: Recursive using DFS. Runtime: 44 ms, faster than 49.47% of Python3 online submissions for Maximum Depth of Binary Tree.

Solution2: Level order traversal using queue. Runtime: 36 ms, faster than 92.25% of Python3 online submissions for Maximum Depth of Binary Tree.

See [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)