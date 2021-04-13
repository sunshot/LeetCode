class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # can not detect the min element
                if target in nums:
                    return True
                else:
                    return False
        minIndex = left
        # print(f'min:{minIndex}')
        if target == nums[minIndex]:
            return True
        left = 0
        if target < nums[left]:
            left = minIndex
        right = len(nums) - 1
        if target > nums[right]:
            right = minIndex - 1
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return True
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

if __name__== '__main__':
    solution = Solution()
    
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    ans = solution.search(nums, target)
    print(ans)      
