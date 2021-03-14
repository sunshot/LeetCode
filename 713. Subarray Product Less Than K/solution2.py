from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        left = 0
        right = 0
        prod = 1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod = prod // nums[left]
                left += 1
            ans += right - left + 1
        return ans
            
if __name__== '__main__':
    solution = Solution()

    nums = [10,5,2,6]
    k = 10
    ans = solution.numSubarrayProductLessThanK(nums, k)
    print(ans == 3)
