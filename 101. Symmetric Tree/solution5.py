from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        queue = collections.deque([])
        queue.append(root)
        while queue:
            level = len(queue)
            curr = []
            hasChild = False
            for _ in range(level):
                node = queue.popleft()
                if not node:
                    curr.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    curr.append(node.val)
                    if node.left:
                        hasChild = True
                        queue.append(node.left)
                    else:
                        queue.append(None)
                    if node.right:
                        hasChild = True
                        queue.append(node.right)
                    else:
                        queue.append(None)
            
            # detect curr symmetric
            left = 0
            right = len(curr) - 1
            while left < right:
                if curr[left] == curr[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            if not hasChild:
                return True
        
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

    # nums = [1,2,2,3,4,4,3]
    nums = [1,2,2,'null',3,'null',3]
    ans = solution.isSymmetric(convert2TreeNode(nums))
    print(ans)