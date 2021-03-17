# [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

```

Similar Problems:

- [112. Path Sum](https://leetcode.com/problems/path-sum/)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

思路：比 112 和 113 明显更难，对每一个遍历到的节点，都需要判断是否有路径存在，并且有多少条？DFS 加上 prefix sum 的思路，对每一个节点，记录 root 到这个节点的 prefix sum 及这个 prefix sum 的个数，然后判断以此节点结束有多少条路径，通过 curr prefix sum - targetSum 是否在 hash 中进行判断

需要注意的是，递归函数：

``def dfs(node, currSum):``

currSum 是一个标量，因此，函数里面对它的修改，调用它的父函数是看不到的，因此不需要恢复

```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.ans = 0
        self.prefixsum = collections.defaultdict(int)
        self.prefixsum[0] = 1
        def dfs(node, currSum):
            if node:
                currSum += node.val
                self.ans += self.prefixsum[currSum - targetSum]
                self.prefixsum[currSum] += 1
                dfs(node.left, currSum)
                dfs(node.right, currSum)
                self.prefixsum[currSum] -= 1
        dfs(root, 0)
        return self.ans
```
