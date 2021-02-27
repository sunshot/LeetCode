from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        curr = 1
        unique = 0
        while curr < len(nums):
            if nums[curr] != nums[unique]:
                unique += 1
                if unique != curr:
                    nums[unique] = nums[curr]
            curr += 1
        while unique+1 < len(nums):
            nums.pop()
        return len(nums)

if __name__== '__main__':
    solution = Solution()

    nums = [0,0,1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(nums)
    print(result == 5)
    print(nums)