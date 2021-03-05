from typing import List
import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = 0
        right = left + k
        result = []
        windows = sorted(nums[left:right])
        while right <= len(nums):
            if k % 2 == 0:
                index = k // 2
                median = (windows[index-1] + windows[index]) / 2.0
            else:
                index = (k - 1) // 2
                median = windows[index]
            result.append(median)
            if right < len(nums):
                a = nums[left]
                b = nums[right]
                windows.remove(a)
                bisect.insort(windows, b)
            left += 1
            right += 1
        return result
        
if __name__== '__main__':
    solution = Solution()

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solution.medianSlidingWindow(nums, k)
    print(result)