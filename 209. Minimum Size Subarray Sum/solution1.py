from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        result = float("inf")
        curr = 0
        while right < len(nums):
            curr += nums[right]
            
            while left <= right and curr >= target:
                if right + 1 -left < result:
                    result = right + 1 -left
                curr -= nums[left]
                left += 1
            
            right += 1
        if result == float("inf"):
            return 0
        else:
            return result

if __name__== '__main__':
    solution = Solution()

    nums = [2,3,1,2,4,3]
    target = 7
    result = solution.minSubArrayLen(target, nums)
    print(result)