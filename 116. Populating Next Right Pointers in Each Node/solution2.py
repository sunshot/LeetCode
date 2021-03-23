from typing import List
import collections
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        
        level_start = root
        while level_start:
            curr = level_start
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.right and curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            
            level_start = level_start.left
        
        return root
                
def convert2TreeNode(nums: List[int]) -> Node:
    nodes = []
    for num in nums:
        if str(num) == 'null' or num == None:
            nodes.append(None)
        else:
            node = Node(num)
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

    nums = [1,2,3,4,5,6,7]
    root = convert2TreeNode(nums)
    root = solution.connect(root)
    
    ans = []
    q = collections.deque([root])

    while q:
        node = q.popleft()
        ans.append(node.val)
        if not node.next:
            ans.append('#')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    print(ans)