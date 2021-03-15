from typing import Tuple
from typing import List
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
        

def convert2TreeNode(nums: List[int]) -> TreeNode:
    nodes = []
    for num in nums:
        if str(num) == 'null' or num == None:
            nodes.append(None)
        else:
            node = TreeNode(num)
            nodes.append(node)
    if not nodes or len(nodes) == 0:
        return None
    curr = 0
    level = 0
    next_child = 2 ** level
    while next_child < len(nodes):
        for i in range(curr, curr + 2 ** level):
            if nodes[i]:
                nodes[i].left = nodes[next_child]
                nodes[i].right = nodes[next_child + 1]
            next_child += 2
        curr = i + 1
        level += 1
    return nodes[0]

if __name__== '__main__':
    solution = Solution()

    # nums = [3,2,3,'null',3,'null',1]
    nums = [3,4,5,1,3,'null',1]
    root = convert2TreeNode(nums)
    # print(root.val)

    ans = solution.rob(root)
    # print(ans == 7)
    print(ans == 9)

