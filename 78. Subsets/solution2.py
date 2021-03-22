from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans.append([])
        
        for num in nums:
            ans += [curr + [num] for curr in ans]
        
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3]
    ans = solution.subsets(nums)
    print(ans)