from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            other = target - nums[i]
            if other in nums[i+1:]:
                index = nums.index(other, i+1)
                result = [i, index]
                return result
        return None
        
if __name__== '__main__':
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    ans = solution.twoSum(nums, target)
    print(ans)