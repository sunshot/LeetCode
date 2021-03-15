from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        currSum = 0
        for left in range(n-1, -1, -1):
            currSum += nums[left]
            if currSum >= x:
                break
        if currSum < x:
            return -1
        result = float("inf")
        double = nums * 2
        right = n - 1
        if currSum == x:
            result = right - left + 1
        right += 1
        while right < len(double) and left < n+1:
            currSum += double[right]
            while left < n+1 and currSum > x:
                currSum -= double[left]
                left += 1
            if left < n+1 and currSum == x:
                if right + 1 -left < result:
                    result = right + 1 -left
            right += 1
        if result == float("inf"):
            return -1
        else:
            return result
        
if __name__== '__main__':
    solution = Solution()

    nums = [3,2,20,1,1,3]
    x = 10
    ans = solution.minOperations(nums, x)
    print(ans)