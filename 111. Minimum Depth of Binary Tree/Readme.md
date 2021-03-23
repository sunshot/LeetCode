# [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

```
Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

```

Constraints:

- The number of nodes in the tree is in the range [0, 10^5].
- -1000 <= Node.val <= 1000

Solution1: Level order traversal using queue. Runtime: 484 ms, faster than 78.18% of Python3 online submissions for Minimum Depth of Binary Tree.

Solution2: https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36045/My-4-Line-java-solution Recursive using DFS.

```java
public static int minDepth(TreeNode root) {
    if (root == null) return 0;
    if (root.left == null) return minDepth(root.right) + 1;
    if (root.right == null) return minDepth(root.left) + 1;
    return Math.min(minDepth(root.left),minDepth(root.right)) + 1;
}
```

https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36239/Python-BFS-and-DFS-solutions.
