from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        # backtrack
        def backtrack(path: List[int], index: int) -> None:
            if len(path) > len(nums):
                return
            if index > len(nums):
                return
            ans.append(path)
            
            for i in range(index, len(nums)):
                backtrack(path + [nums[i]], i + 1)
        
        backtrack([], 0)
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3]
    ans = solution.subsets(nums)
    print(ans)