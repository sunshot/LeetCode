from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # result = []
        p_ancestor = []
        p_level = -1
        q_ancestor = []
        q_level = -1
        #node, level, status
        stack = [[root, 0, 0]]
        while stack:
            node, level, status = stack[-1]
            if status == 1:
                # result.append((node.val,level))
                stack.pop()
                if node == p:
                    p_level = level
                    p_ancestor.append(node)
                elif p_level == level + 1:
                    p_ancestor.append(node)
                    p_level = level
                if node == q:
                    q_level = level
                    q_ancestor.append(node)
                elif q_level == level + 1:
                    q_ancestor.append(node)
                    q_level = level
            else:
                stack[-1][2] = 1
                if node.right:
                    stack.append([node.right, level+1, 0])
                if node.left:
                    stack.append([node.left, level+1, 0])
            
        # print(p_ancestor)
        # print(q_ancestor)
        # print(result)
        ret = [node for node in p_ancestor if node in q_ancestor]
        if ret:
            return ret[0]
        else:
            return None
        
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

def findTreeNode(root: TreeNode, num: int) -> TreeNode:
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == num:
            return node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return None


if __name__== '__main__':
    solution = Solution()

    nums = [3,5,1,6,2,0,8,'null','null',7,4]
    root = convert2TreeNode(nums)
    p = findTreeNode(root, 5)
    q = findTreeNode(root, 1)
    
    ans = solution.lowestCommonAncestor(root, p, q)
    print(ans.val)