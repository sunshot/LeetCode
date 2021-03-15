from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return None
        n = len(nums)
        if n == 3:
            return nums[0] * nums[1] * nums[2]
        sort_nums = sorted(nums)
        candidates = [sort_nums[-1] * sort_nums[-2] * sort_nums[-3], sort_nums[0] * sort_nums[1] * sort_nums[-1]]
        return max(candidates)
        
if __name__== '__main__':
    solution = Solution()

    nums = [-3,-2,-1,-1,1,6]
    ans = solution.maximumProduct(nums)
    print(ans)
    