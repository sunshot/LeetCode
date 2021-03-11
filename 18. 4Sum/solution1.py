from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                left = j+1
                right = n-1
                while left < right:
                    foursum = nums[i] + nums[j] + nums[left] + nums[right]
                    if foursum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif foursum > target:
                        right -= 1
                    else:
                        left += 1
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,0,-1,0,-2,2]
    target = 0
    ans = solution.fourSum(nums, target)
    print(ans)

