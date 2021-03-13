from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) <= 1:
            return False
        if k < 0:
            k = -k
        for i in range(1, len(nums)):
            if nums[i] == 0 and nums[i-1] == 0:
                return True
        if k == 0:
            return False
        currSum = 0
        # d is mod : index
        d = {0:-1}
        for i, num in enumerate(nums):
            currSum += num
            mod = currSum % k
            if mod in d:
                if i - d[mod] >= 2:
                    return True
            else:
                d[mod] = i
            # print(d)
        return False

if __name__== '__main__':
    solution = Solution()

    nums = [23,2,4,6,7]
    k = -6
    print(solution.checkSubarraySum(nums, k))