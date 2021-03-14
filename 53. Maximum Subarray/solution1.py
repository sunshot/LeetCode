from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = [None] * len(nums)
        maxsum[0] = nums[0]
        for i in range(1, len(nums)):
            maxsum[i] = max(maxsum[i-1]+nums[i], nums[i])
        return max(maxsum)

if __name__== '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = solution.maxSubArray(nums)
    print(ans)