from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color = {}
        for x in nums:
            if x in color:
                color[x] += 1
            else:
                color[x] = 1
        ele = [0, 1, 2]
        i = 0
        for x in ele:
            if x in color:
                for j in range(color[x]):
                    nums[i] = x
                    i += 1

if __name__== '__main__':
    solution = Solution()

    nums = [2,0,2,1,1,0]
    solution.sortColors(nums)
    print(nums == [0,0,1,1,2,2])