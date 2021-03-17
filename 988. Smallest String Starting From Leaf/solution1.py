from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return None
        leafnodes = []
        parents = {root:None}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if not node.right and not node.left:
                leafnodes.append(node)
        # sort leafnodes
        leafnodes.sort(key=lambda node: node.val)
        mininode = leafnodes[0]
        mininodes = [mininode]
        for i in range(1, len(leafnodes)):
            if leafnodes[i].val == mininode.val:
                mininodes.append(leafnodes[i])
            else:
                break
        results = []
        for node in mininodes:
            curr = node
            result = ''
            while curr:
                result += chr(ord('a')+curr.val)
                curr = parents[curr]
            results.append(result)
        result = results[0]
        for i in range(1, len(results)):
            if results[i] < result:
                result = results[i]
        return result

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

    nums = [0,1,2,3,4,3,4]
    root = convert2TreeNode(nums)

    ans = solution.smallestFromLeaf(root)
    print(ans)