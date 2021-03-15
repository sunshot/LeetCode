from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # index: cumulative sum up to index, and includes index
        d = {-1:0}
        for i, num in enumerate(nums):
            d[i] = d[i-1] + num
        for i in range(len(nums)):
            left = d[i-1]
            right = d[len(nums) - 1] - d[i]
            if left == right:
                return i
        return -1

if __name__== '__main__':
    solution = Solution()

    nums = [1,7,3,6,5,6]
    ans = solution.pivotIndex(nums)
    print(ans)