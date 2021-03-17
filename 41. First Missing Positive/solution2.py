from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = float('inf')
        mask = 0
        for i in nums:
            if i>0 and i<=len(nums):
                min_num = min(i, min_num)
                mask |= (1<<i)
        if min_num > 1:
            return 1
        for i in range(min_num, min_num+len(nums)):
            if mask & (1<<i) == 0:
                return i
        return min_num+len(nums)

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,0]
    # nums = [3,4,-1,1]
    ans = solution.firstMissingPositive(nums)
    print(ans)

