from typing import List
from typing import Tuple
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        def dfs(node: TreeNode) -> Tuple[int, TreeNode]:
            if not node:
                return (0, None)
            h1, lca1 = dfs(node.left)
            h2, lca2 = dfs(node.right)
            if h1 > h2:
                return (h1 + 1, lca1)
            if h1 < h2:
                return (h2 + 1, lca2)
            return (h1 + 1, node)
        
        return dfs(root)[1]
                    
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

def levelOrderTraversal(root: TreeNode) -> List[int]:
    ans = []
    q = collections.deque([root])
    while q:
        node = q.popleft()
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans

if __name__== '__main__':
    solution = Solution()

    nums = [3,5,1,6,2,0,8,'null','null',7,4]
    root = convert2TreeNode(nums)

    ans = solution.subtreeWithAllDeepest(root)
    print(levelOrderTraversal(ans))