from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.ans = False
        def dfs(node, A):
            if node:
                if self.ans:
                    return
                A.append(node.val)
                if not node.left and not node.right:
                    theSum = sum(A)
                    if theSum == targetSum:
                        self.ans = True
                        return

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()
        dfs(root, [])
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

    nums = [5,4,8,11,'null',13,4,7,2,'null','null','null',1]
    targetSum = 22
    root = convert2TreeNode(nums)

    ans = solution.hasPathSum(root, targetSum)
    print(ans)
