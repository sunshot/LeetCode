# [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Examples:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

```

Constraints:

- The number of nodes in the tree will be in the range [1, 500].
- 0 <= Node.val <= 500
- The values of the nodes in the tree are unique.

Hints from 1123:

- Do a postorder traversal.
- Then, if both subtrees contain a deepest leaf, you can mark this node as the answer (so far).
- The final node marked will be the correct answer.

Solution1: Refer to [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/). Use parents dicts to record child:parent relationship. And then postorder traversal to find the depthest nodes and their lowest common ancestor. (Seem anyother traversal is also OK?)

Runtime: 32 ms, faster than 85.49% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.


Solution2: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solution/

We try a straightforward approach that has two phases.

The first phase is to identify the nodes of the tree that are deepest. To do this, we have to annotate the depth of each node. We can do this with a depth first search.

Afterwards, we will use that annotation to help us find the answer:

- If the node in question has maximum depth, it is the answer.

- If both the left and right child of a node have a deepest descendant, then the answer is this parent node.

- Otherwise, if some child has a deepest descendant, then the answer is that child.

- Otherwise, the answer for this subtree doesn't exist.

关键思想：如果某个节点的左右孩子都是最深的节点，则此节点为所求答案，然后递归的进行。实现的时候，可以用一个递归函数实现： ``def dfs(node: TreeNode) -> Tuple[int, TreeNode]:`` 返回 node 子树的高度，以及最深节点的最小祖先节点，然后递归的进行即可

Runtime: 36 ms, faster than 64.03% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.


https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/146808/C%2B%2BJavaPython-One-Pass

