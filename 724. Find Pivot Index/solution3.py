from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        totalSum = sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == (totalSum - leftsum - num):
                return i
            leftsum += num
        return -1
        
if __name__== '__main__':
    solution = Solution()

    nums = [1,7,3,6,5,6]
    ans = solution.pivotIndex(nums)
    print(ans)