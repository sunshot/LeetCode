class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        minIndex = left
        if target == nums[minIndex]:
            return minIndex
        left = 0
        if target < nums[left]:
            left = minIndex
        right = len(nums) - 1
        if target > nums[right]:
            right = minIndex - 1
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
      
if __name__== '__main__':
    solution = Solution()
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans = solution.search(nums, target)
    print(ans)      
