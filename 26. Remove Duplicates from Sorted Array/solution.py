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