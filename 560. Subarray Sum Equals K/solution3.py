from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        currSum = 0
        sumHash = {}
        sumHash[0] = 1
        ans = 0
        for i, num in enumerate(nums):
            currSum = currSum + num
            if currSum - k in sumHash:
                ans += sumHash[currSum - k]
            sumHash[currSum] = sumHash.get(currSum, 0) + 1
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3]
    k = 3
    ans = solution.subarraySum(nums, k)
    print(ans)