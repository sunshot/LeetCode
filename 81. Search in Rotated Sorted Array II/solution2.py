class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            mid = left + (right - left)//2
            # print(f'left:{left} right:{right} mid:{mid}')
            if target == nums[left]:
                return True
            if target == nums[right]:
                return True
            if target == nums[mid]:
                return True
            
            if target < nums[left]:
                if target < nums[mid] and nums[left] >= nums[mid]:
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
        
        return False
if __name__== '__main__':
    solution = Solution()
    
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    ans = solution.search(nums, target)
    print(ans)              
