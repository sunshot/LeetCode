from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        curr = 0
        unique = -1
        for curr in range(len(nums)):
            if nums[curr] != val:
                unique += 1
                if unique != curr:
                    nums[unique] = nums[curr]
        return unique+1
                
if __name__== '__main__':
    solution = Solution()

    nums = [3,2,2,3]
    val = 3
    ans = solution.removeElement(nums, val)
    # print(ans)
    print(nums[:ans])