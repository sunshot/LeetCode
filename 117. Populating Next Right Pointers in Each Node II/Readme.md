# [117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

Given a binary tree

```c
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

```

Constraints:

- The number of nodes in the given tree is less than 6000.
- -100 <= node.val <= 100 

Solution1: Time complexity: O(n), Space complexity: O(n). Same level order traversal as 116's soluiton1. Runtime: 48 ms, faster than 76.59% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

Solution2: Similar to 116's Solution2, Simply do it level by level, using the next-pointers of the current level to go through the current level and set the next-pointers of the next level. 

Runtime: 44 ms, faster than 90.64% of Python3 online submissions for Populating Next Right Pointers in Each Node II.

