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
        if not root:
            return root
        
        level_start = root
        while level_start:
            curr = level_start
            isUpdateLevelStart = False
            while curr:
                leftchild = None
                firstchild = None
                if curr.left and curr.right:
                    curr.left.next = curr.right
                    leftchild = curr.right
                    firstchild = curr.left
                else:
                    if curr.left:
                        leftchild = curr.left
                    elif curr.right:
                        leftchild = curr.right
                    firstchild = leftchild
                if firstchild and not isUpdateLevelStart:
                    isUpdateLevelStart = True
                    level_start = firstchild
                
                if leftchild:
                    rightchild = None
                    while curr.next and not rightchild:
                        if curr.next.left:
                            rightchild = curr.next.left
                        elif curr.next.right:
                            rightchild = curr.next.right
                        else:
                            curr = curr.next
                    if rightchild:
                        leftchild.next = rightchild
                        
                
                curr = curr.next
            
            if not isUpdateLevelStart:
                level_start = None

                
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

    # nums = [1,2,3,4,5,'null',7]
    # nums = [0,2,4,1,'null',3,-1,5,1,'null',6,'null',8]
    nums = [0,2,4,1,'null',3,-1,5,1,'null','null','null',8]
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