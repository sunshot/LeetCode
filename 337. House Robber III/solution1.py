from typing import Tuple
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # return max_with_node, max_without_node
    def rob_tree(self, node: TreeNode) -> Tuple[int, int]:
        if not node:
            return (0, 0)
        if not node.left and not node.right:
            return (node.val, 0)
        left_max_with_node, left_max_without_node = self.rob_tree(node.left)
        right_max_with_node, right_max_without_node = self.rob_tree(node.right)
        max_with_node = left_max_without_node + node.val + right_max_without_node
        max_without_node = max(left_max_with_node, left_max_without_node) + max(right_max_with_node, right_max_without_node)
        return (max_with_node, max_without_node)
        
    def rob(self, root: TreeNode) -> int:
        max_with_node, max_without_node = self.rob_tree(root)
        return max(max_with_node, max_without_node)
        