from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findIndex(isLeft):
            left = 0
            right = len(nums)
            
            while left < right:
                mid = left + (right - left)//2
                if nums[mid] > target or (isLeft and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        leftIdx = findIndex(True)
        if leftIdx == len(nums) or nums[leftIdx] != target:
            return [-1,-1]
        rightIdx = findIndex(False) - 1
        return [leftIdx, rightIdx]


if __name__== '__main__':
    solution = Solution()

    nums = [5,7,7,8,8,10]
    target = 8
    # target = 6

    ans = solution.searchRange(nums, target)
    print(ans)        