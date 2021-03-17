from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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

    nums = [10,5,-3,3,2,'null',11,3,-2,'null',1]
    targetSum = 8
    root = convert2TreeNode(nums)

    ans = solution.pathSum(root, targetSum)
    print(ans)