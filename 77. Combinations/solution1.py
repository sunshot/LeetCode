from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        if k > n:
            return ans
        
        def backtrack(path: List[int], index: int) -> None:
            if len(path) == k:
                ans.append(path)
                return
            if index > n:
                return
            for i in range(index, n+1):
                backtrack(path + [i], i + 1)
        
        
        backtrack([], 1)
        return ans

if __name__== '__main__':
    solution = Solution()

    n = 4
    k = 2

    ans = solution.combine(n, k)
    print(ans)