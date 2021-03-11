from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        ans = []
        i = 0
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i+1
            right = len(nums) - 1
            while left < right:
                twosum = nums[left] + nums[right]
                if twosum == target:
                    result = [nums[i], nums[left], nums[right]]
                    ans.append(result)
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif twosum > target:
                    # Need to decrease twosum
                    right -= 1
                else:
                    # Need to increase twosum
                    left += 1
        return ans

if __name__== '__main__':
    solution = Solution()

    # nums = [0,0,0,0]
    nums = [-1,0,1,2,-1,-4]
    ans = solution.threeSum(nums)
    print(ans)