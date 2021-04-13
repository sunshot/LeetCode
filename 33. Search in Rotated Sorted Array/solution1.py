from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            # print(f'left:{left} right:{right} mid:{mid}')
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            if target == nums[mid]:
                return mid
            
            if target < nums[left]:
                if target < nums[mid] and nums[left] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if nums[left] < nums[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
      
if __name__== '__main__':
    solution = Solution()
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans = solution.search(nums, target)
    print(ans)
