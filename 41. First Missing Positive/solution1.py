from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            i = i+1
        start = 1
        while i < len(nums):
            if nums[i] > start:
                return start
            elif nums[i] == start:
                i = i+1
                start = start + 1
            else:
                i = i+1
        return start

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,0]
    # nums = [3,4,-1,1]
    ans = solution.firstMissingPositive(nums)
    print(ans)