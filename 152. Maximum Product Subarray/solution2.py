from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return None
        ans = nums[0]
        # curr_max records the max product until the end of curr index
        # curr_min records the min product until the end of curr index
        # We need both as we may have nagetive integer
        curr_max = ans
        curr_min = ans
        for i in range(1, len(nums)):
            candidates = (nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_max = max(candidates)
            curr_min = min(candidates)
            ans = max(ans, curr_max)
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [-2,0,-1,-5, 0, 6, 1, 2, 0, 10]
    ans = solution.maxProduct(nums)
    print(ans)