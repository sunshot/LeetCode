# [988. Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/)

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

```
Input: [0,1,2,3,4,3,4]
Output: "dba"
```

Note:

1. The number of nodes in the given tree will be between 1 and 8500.
1. Each node in the tree will have a value between 0 and 25.

Similar Problems:

- [112. Path Sum](https://leetcode.com/problems/path-sum/)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
- [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

Solution1: 借鉴 [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) 利用 parents = {root:None} 来保存每个节点的父节点，用于恢复路径。第一次 DFS 遍历，获取了 parents dicts 和叶子节点的信息。然后将叶子节点排序，只取最小的相等的叶子节点，对这些最小的叶子节点，恢复出叶子节点到根节点的路径字符串，最后比较这些字符串

Solution2: 递归 DFS 解法，其实最小字符串用 python 的 min 函数进行比较就行，问题转化为 DFS 遍历树，记录根到叶子节点的路径，但节点为叶子节点时，形成字符串，看是否时最小的字符串。与 129 112 等都很像

char convert to int using python

```python
>>> chr(97) 
'a' 
>>> ord('a') 
97
```
