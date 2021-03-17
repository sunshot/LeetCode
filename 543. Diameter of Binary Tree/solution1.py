from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        
        def diameter(node):
            if not node:
                return 0
            left_length = diameter(node.left)
            right_length = diameter(node.right)
            if node.left:
                left_length += 1
            if node.right:
                right_length += 1
            self.ans = max(self.ans, left_length+right_length)
            return max(left_length, right_length)
        
        diameter(root)
        return self.ans
            
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
                nodes[i].left = nodes[next_child] if next_child < len(nodes) else None
                nodes[i].right = nodes[next_child + 1] if next_child + 1 < len(nodes) else None
                next_child += 2
        curr = i + 1
        level += 1
    return nodes[0]

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3,4,5]
    root = convert2TreeNode(nums)

    ans = solution.diameterOfBinaryTree(root)
    print(ans)