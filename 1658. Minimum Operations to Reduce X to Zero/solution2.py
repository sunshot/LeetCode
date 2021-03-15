from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x
        for num in nums:
            target += num
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        # cumulative sum : index
        d = {0:-1}
        ans = -float("inf")
        cumSum = 0
        for i, num in enumerate(nums):
            cumSum += num
            if cumSum - target in d:
                ans = max(ans, i - d[cumSum - target])
            d[cumSum] = i
        if ans == -float("inf"):
            return -1
        else:
            return len(nums) - ans

        
if __name__== '__main__':
    solution = Solution()

    nums = [3,2,20,1,1,3]
    x = 10
    ans = solution.minOperations(nums, x)
    print(ans)