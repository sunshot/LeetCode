# [815. Bus Routes](https://leetcode.com/problems/bus-routes/)

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

- For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

```
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
```

Constraints:

- 1 <= routes.length <= 500.
- 1 <= routes[i].length <= 10^5
- All the values of routes[i] are unique.
- sum(routes[i].length) <= 10^5
- 0 <= routes[i][j] < 10^6
- 0 <= source, target < 10^6

Solution: https://leetcode.com/problems/bus-routes/solution/ BFS

构建一个图，然后采用BFS搜索，题目问的是需要多少趟 bus，因此只需要构建 bus 之间的关系图，如果两个bus之间有共有的 bus stop，则认为这两个bus之间有一条边，即bus作为节点。


