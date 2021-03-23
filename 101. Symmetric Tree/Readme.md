# [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

```
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
```

Constraints:

- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

Solution1: 笨办法，采用层序遍历，对这一层的 value 进行判断，是否对称，如果某个节点没有左或右子树，加一个 mockup 节点。 O(n^2). 8868 ms	730.9 MB

Solution2: see https://leetcode.com/problems/symmetric-tree/solution/.  Each two consecutive nodes in the queue should be equal, and their subtrees a mirror of each other. Initially, the queue contains root and root. Then the algorithm works similarly to BFS, with some key differences. Each time, two nodes are extracted and their values compared. Then, the right and left children of the two nodes are inserted in the queue in opposite order. The algorithm is done when either the queue is empty, or we detect that the tree is not symmetric (i.e. we pull out two consecutive nodes from the queue that are unequal). Runtime: 32 ms, faster than 82.46% of Python3 online submissions for Symmetric Tree.

Solution3: 递归

Two trees are a mirror reflection of each other if:

- Their two roots have the same value.
- The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
Runtime: 36 ms, faster than 59.80% of Python3 online submissions for Symmetric Tree.

Solution4: Improve based on Solution3. We do not need to do ``isMirror(root, root)``, after we make sure root is not null, we can just do ``isMirror(root.left, root.right)``.  Runtime: 24 ms, faster than 98.97% of Python3 online submissions for Symmetric Tree. Great improvement.

Solution5: Improve based on Solution1, just add None instread of dummy TreeNode. 1204 ms	65.3 MB

Similar Problems:

- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)
- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
