# [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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

Examples:

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

```

Constraints:

- The number of nodes in the given tree is less than 4096.
- -1000 <= node.val <= 1000

Solution1: Level order traversal. And for each level, connect next pointer.

Runtime: 68 ms, faster than 40.01% of Python3 online submissions for Populating Next Right Pointers in Each Node.


Solution2:

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37461/Java-solution-with-O(1)-memory%2B-O(n)-time

Runtime: 64 ms, faster than 62.19% of Python3 online submissions for Populating Next Right Pointers in Each Node.

Idea：因为 perfect binary tree where all leaves are on the same level, and every parent has two children，因此每一层的开始节点的 left 即是下一层的开始节点。从每一层的起始节点开始，设为 curr，先将 curr.left.next = curr.right，然后如果 curr.right and curr.next，则将 curr.right.next = curr.next.left，同时 curr = curr.next，直到 curr 为 None。即每次对每一层节点循环时，将下一层节点的next赋值。

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space

Simply do it level by level, using the next-pointers of the current level to go through the current level and set the next-pointers of the next level.

Solution3: Recursive. 还是利用每一层的 next pointer 来进行递归
