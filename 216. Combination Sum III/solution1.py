from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        minSum = 0
        for i in range(1, k+1):
            minSum += i
        if n < minSum:
            return []
        ans = []
        
        # backtrack
        def backtrack(path: List[int], index: int, target: int) -> None:
            if target == 0 and len(path) == k:
                ans.append(path)
            if target < 0:
                return
            if len(path) > k:
                return
            if index >= 10:
                return
            for i in range(index, 10):
                if target - i < 0:
                    continue
                backtrack(path + [i], i + 1, target - i)
        
        backtrack([], 1, n)
        return ans


if __name__== '__main__':
    solution = Solution()

    k = 3
    n = 7

    ans = solution.combinationSum3(k, n)
    print(ans)