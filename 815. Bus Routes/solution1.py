from typing import List
import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if not routes:
            return -1
        if source == target:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                shared = r1.intersection(r2)
                if shared and len(shared) > 0:
                    graph[i].add(j)
                    graph[j].add(i)
        visited, targets = set(), set()
        for i, route in enumerate(routes):
            if source in route:
                visited.add(i)
            if target in route:
                targets.add(i)
        queue = collections.deque([(node, 1) for node in visited])
        while queue:
            node, depth = queue.popleft()
            if node in targets: 
                return depth
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, depth+1))
        return -1


if __name__== '__main__':
    solution = Solution()

    routes = [[1,2,7],[3,6,7]]
    source = 1
    target = 6
    ans = solution.numBusesToDestination(routes, source, target)
    print(ans)