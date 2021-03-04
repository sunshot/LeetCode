from typing import List
class Solution:
    def search(self, target: int, sums: List[int], left: int, right: int, n: int) -> int:
        while left < right:
            mid = (left + right) // 2
            if n - sums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        result = float("inf")
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i]
        for right in range(len(sums)):
            # indicate nums 0..right sum
            n = sums[right]
            if n >= target:
                left = self.search(target, sums, left, right, n)
                result = min(result, right+1 - left)
            
        if result == float("inf"):
            return 0
        else:
            return result

if __name__== '__main__':
    solution = Solution()

    nums = [2,3,1,2,4,3]
    target = 7
    result = solution.minSubArrayLen(target, nums)
    print(result)