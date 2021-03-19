from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        if not candidates or len(candidates) == 0:
            return ans
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                result = [candidates[0]] * (target // candidates[0])
                ans.append(result)
            return ans
        # backtrack
        def backtrack(path: List[int], index: int) -> None:
            if sum(path) == target:
                ans.append(path.copy())
                return
            elif sum(path) > target:
                return
            if len(path) > 150:
                return
            if index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i)
                path.pop()
        
        backtrack([], 0)
        return ans
if __name__== '__main__':
    solution = Solution()

    candidates = [2,3,6,7]
    target = 7

    ans = solution.combinationSum(candidates, target)
    print(ans)