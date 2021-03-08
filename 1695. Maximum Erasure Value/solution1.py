from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return None
        digiIndex = {}
        start = 0
        result = 0
        for i, digi in enumerate(nums):
            if digi in digiIndex and digiIndex[digi] >= start:
                start = digiIndex[digi] + 1
            else:
                result = max(result, sum(nums[start:i+1]))
            digiIndex[digi] = i
        return result

if __name__== '__main__':
    solution = Solution()

    nums = [5,2,1,2,5,2,1,2,5]
    expected = 8
    result = solution.maximumUniqueSubarray(nums)
    print(result == expected)