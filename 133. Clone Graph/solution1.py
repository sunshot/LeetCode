import collections
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Use BFS to deep copy
        if not node:
            return None
        # Use a dict to keep the mapping
        d = {}
        d[node] = Node(node.val)
        q = collections.deque([node])
        
        while q:
            curr = q.popleft()
            for neigh in curr.neighbors:
                if neigh not in d:
                    d[neigh] = Node(neigh.val)
                    q.append(neigh)
                d[curr].neighbors.append(d[neigh])
            
            
        return d[node]
        