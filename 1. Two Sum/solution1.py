from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in d:
                ans = []
                ans.append(d[val])
                ans.append(i)
                return ans
            else:
                d[num] = i
        return []

if __name__== '__main__':
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    ans = solution.twoSum(nums, target)
    print(ans)