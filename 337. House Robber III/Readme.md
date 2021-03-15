# [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

```
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

Constraints:

- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4

Similar problems:
- [198. House Robber](https://leetcode.com/problems/house-robber/) and in [github](https://github.com/sunshot/LeetCode/tree/main/198.%20House%20Robber)
- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) and in [github](https://github.com/sunshot/LeetCode/tree/main/213.%20House%20Robber%20II)

Solution1: 递归、分治、动态规划，参考 198 的思想，需要分别知道左右子树：max_with_node, max_without_node，然后：

```python
max_with_node = left_max_without_node + node.val + right_max_without_node
max_without_node = max(left_max_with_node, left_max_without_node) + max(right_max_with_node, right_max_without_node)
```

因此可以递归的求的当前树作为根节点的 max_with_node, max_without_node

Runtime: 44 ms, faster than 90.34% of Python3 online submissions for House Robber III.

