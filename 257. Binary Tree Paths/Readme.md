# [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

Constraints:

- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100

Similar Problems

- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- [988. Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/)

递归 DFS，然后记录 root 到当前节点的路径