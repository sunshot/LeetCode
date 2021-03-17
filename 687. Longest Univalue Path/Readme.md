# [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

```
Input: root = [5,4,5,1,1,5]
Output: 2
```

Constraints:

- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
- The depth of the tree will not exceed 1000.

Similar Problems:

- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [250. Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/) Need subscribe

这道题比 437 难，需要弄清楚递归的条件。 See https://leetcode.com/problems/longest-univalue-path/solution/

We can think of any path (of nodes with the same values) as up to two arrows extending from it's root.

Specifically, the root of a path will be the unique node such that the parent of that node does not appear in the path, and an arrow will be a path where the root only has one child node in the path.

Then, for each node, we want to know what is the longest possible arrow extending left, and the longest possible arrow extending right? We can solve this using recursion.

Let arrow_length(node) be the length of the longest arrow that extends from the node. That will be 1 + arrow_length(node.left) if node.left exists and has the same value as node. Similarly for the node.right case.

某个节点的 path，如果与它的父节点相连，则只能从左或者右选取一条 path