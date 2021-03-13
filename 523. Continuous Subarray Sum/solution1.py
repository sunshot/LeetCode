from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) <= 1:
            return False
        if k < 0:
            k = -k
        currSum = 0
        lastSum = 0
        d = set()
        for i, num in enumerate(nums):
            if i == 1:
                d.add(0)
            elif i > 1:
                d.add(lastSum)
            lastSum = currSum
            currSum += num
            if k == 0:
                if currSum in d:
                    return True
                continue
            if i > 0 and currSum % k == 0:
                return True
            n = currSum // k
            if n+1 > len(d):
                for x in d:
                    target = currSum - x
                    if target % k == 0:
                        return True
            else:
                for i in range(n+1):
                    target = currSum - i*k
                    if target in d:
                        return True
        return False
        
if __name__== '__main__':
    solution = Solution()

    nums = [23,2,4,6,7]
    k = -6
    print(solution.checkSubarraySum(nums, k))