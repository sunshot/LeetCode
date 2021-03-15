from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        # d[i]: cumulative sum for 0..i-1
        d = [0] * (n+1)
        for i, num in enumerate(nums):
            d[i+1] = d[i] + num
        for i in range(len(nums)):
            left = d[i]
            right = d[-1] - d[i+1]
            if left == right:
                return i
        return -1

if __name__== '__main__':
    solution = Solution()

    nums = [1,7,3,6,5,6]
    ans = solution.pivotIndex(nums)
    print(ans)