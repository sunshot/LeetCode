from typing import List
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        sumDict = {-1:0}
        sumHash = collections.defaultdict(int)
        for i, num in enumerate(nums):
            sumDict[i] = sumDict[i-1] + num
            sumHash[sumDict[i]] += 1
        ans = 0
        for i in range(len(nums)):
            target = k + sumDict[i-1]
            ans += sumHash[target]
            # Now we need to delete sumDict[i] from hash
            sumHash[sumDict[i]] -= 1
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3]
    k = 3
    ans = solution.subarraySum(nums, k)
    print(ans)