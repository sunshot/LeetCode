from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 2:
            return []
        if nums[0] + nums[1] > target or nums[-1] + nums[-2] < target:
            return []
        ans = []
        left = 0
        right = len(nums) - 1
        while left < right:
            twosum = nums[left] + nums[right]
            if twosum > target:
                right -= 1
            elif twosum < target:
                left += 1
            else:
                ans.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
        return ans
    
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        if not nums or len(nums) < k:
            return []
        if sum(nums[0:k]) > target or nums[-1] * k < target:
            return []
        if k == 2:
            return self.twoSum(nums, target)
        ans = []
        for i in range(len(nums)+1-k):
            if i == 0 or nums[i] != nums[i-1]:
                for _, res in enumerate(self.kSum(nums[i+1:], target - nums[i], k - 1)):
                    ans.append([nums[i]] + res)
        return ans
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        return self.kSum(nums, target, 4)

if __name__== '__main__':
    solution = Solution()

    nums = [1,0,-1,0,-2,2]
    target = 0
    ans = solution.fourSum(nums, target)
    print(ans)