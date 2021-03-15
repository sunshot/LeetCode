from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if p == 1:
            return 0
        currSum = sum(nums)
        target = currSum % p
        if target == 0:
            return 0
        # cumulative sum % p : latest index
        d = {0:-1}
        currSum = 0
        ans = float('inf')
        for i, num in enumerate(nums):
            currSum += num
            mod = currSum % p
            target_mod = mod - target
            if target_mod < 0:
                target_mod += p
            if target_mod in d:
                ans = min(ans, i - d[target_mod])
            d[mod] = i
        if ans == float('inf') or ans == len(nums):
            return -1
        else:
            return ans
            
if __name__== '__main__':
    solution = Solution()

    nums = [3,1,4,2]
    p = 6
    ans = solution.minSubarray(nums, p)
    print(ans == 1)