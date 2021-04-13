class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
if __name__== '__main__':
    solution = Solution()
    
    nums = [4,5,6,7,0,1,2]
    ans = solution.findMin(nums)
    
    print(ans)
