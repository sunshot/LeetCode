from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[grid[i][j] for j in range(n)] for i in range(m)]
        
        # row 0
        for j in range(1, n):
            dp[0][j] += dp[0][j-1]
        
        # col 0
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + dp[i][j]
        
        return dp[m-1][n-1]
        
if __name__== '__main__':
    solution = Solution()

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans = solution.minPathSum(grid)
    print(ans == 7)