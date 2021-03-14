from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        currMax = ans
        for i in range(1, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            ans = max(ans, currMax)
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = solution.maxSubArray(nums)
    print(ans)