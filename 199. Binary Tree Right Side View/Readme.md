# [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
```

Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Solution1: Straightforward, use level order traversal, and for each level, append the last node's value. Runtime: 36 ms, faster than 37.72% of Python3 online submissions for Binary Tree Right Side View. Need to improve.

Solution2: Slightly improvement based on Solution1. Do not compare the level lenghth, add it before the level loop. Runtime: 28 ms, faster than 89.66% of Python3 online submissions for Binary Tree Right Side View.

Solution3: Recursive

https://leetcode.com/problems/binary-tree-right-side-view/discuss/56012/My-simple-accepted-solution(JAVA)

- Each depth of the tree only select one node.
- View depth is current size of result list.

https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms

Runtime: 32 ms, faster than 70.18% of Python3 online submissions for Binary Tree Right Side View.

Similar Problems:

- [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
- [545. Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree) Need to Subscribe. 
