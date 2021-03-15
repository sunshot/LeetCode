from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return None
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
        return max(max1 * max2 * max3, min1 * min2 * max1)

if __name__== '__main__':
    solution = Solution()

    nums = [-3,-2,-1,-1,1,6]
    ans = solution.maximumProduct(nums)
    print(ans)