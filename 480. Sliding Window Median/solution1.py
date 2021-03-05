from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = 0
        right = left + k
        result = []
        while right <= len(nums):
            temp = sorted(nums[left:right])
            if len(temp) % 2 == 0:
                index = len(temp) // 2
                median = (temp[index-1] + temp[index]) / 2.0
            else:
                index = (len(temp) - 1) // 2
                median = temp[index]
            result.append(median)
            left += 1
            right += 1
        return result

if __name__== '__main__':
    solution = Solution()

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solution.medianSlidingWindow(nums, k)
    # expected = [1, -1, -1, 3, 5, 6]
    print(result)