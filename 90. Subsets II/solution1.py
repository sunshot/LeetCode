from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        # backtrack
        def backtrack(path: List[int], index: int) -> None:
            if len(path) > len(nums):
                return
            if index > len(nums):
                return
            ans.append(path)
            
            for i in range(index, len(nums)):
                if i == index or nums[i] != nums[i-1]:
                    backtrack(path + [nums[i]], i + 1)
        
        backtrack([], 0)
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,2,2]
    ans = solution.subsetsWithDup(nums)
    print(ans)