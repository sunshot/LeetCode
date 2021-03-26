from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if nums[right] > target:
                    right -= 1
                elif nums[left] < target:
                    left += 1
                else:
                    # nums[right] = nums[left] = target
                    return [left, right]
            
        return [-1,-1]

if __name__== '__main__':
    solution = Solution()

    nums = [5,7,7,8,8,10]
    # target = 8
    target = 6

    ans = solution.searchRange(nums, target)
    print(ans)