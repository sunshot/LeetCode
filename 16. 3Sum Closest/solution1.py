from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        minClose = abs(nums[l] + nums[r] - target)
        minCurSum = nums[l] + nums[r]
        while l < r:
            curSum = nums[l] + nums[r]
            if abs(curSum - target) < minClose:
                minClose = abs(curSum - target)
                minCurSum = curSum
           
            if curSum > target:
                r = r - 1
                while r>=0 and nums[r] == nums[r+1]:
                    r = r - 1
            elif curSum < target:
                l = l + 1
                while l<len(nums) and nums[l] == nums[l-1]:
                    l = l + 1
            else:
                return (minClose, target)
        return (minClose, minCurSum)
        
            
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return sum(nums)
        nums.sort()
        minCurSum = nums[0] + nums[1] + nums[2]
        minClose = abs(minCurSum - target)
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            two_target = target-nums[i]
            (two_minClose, two_curSum) = self.twoSum(nums[i+1:], two_target)
            if two_minClose == 0:
                return target
            if two_minClose < minClose:
                minClose = two_minClose
                minCurSum = nums[i] + two_curSum
        return minCurSum

if __name__== '__main__':
    solution = Solution()

    nums = [-1,2,1,-4]
    target = 1
    ans = solution.threeSumClosest(nums, target)
    print(ans)