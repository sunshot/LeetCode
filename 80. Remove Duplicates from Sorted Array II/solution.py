class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return len(nums)
        curr = 2
        unique = 1
        for curr in range(2, len(nums)):
            if nums[curr] != nums[unique] or (nums[curr] == nums[unique] and 
                                             nums[curr] != nums[unique-1]):
                unique += 1
                if unique != curr:
                    nums[unique] = nums[curr]
        while unique+1 < len(nums):
            nums.pop()
        return len(nums)