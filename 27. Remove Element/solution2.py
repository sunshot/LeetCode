from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        curr = 0
        n = len(nums)
        while curr < n:
            if nums[curr] == val:
                nums[curr] = nums[n-1]
                n -= 1
            else:
                curr += 1
        return n
                
if __name__== '__main__':
    solution = Solution()

    nums = [3,2,2,3]
    val = 3
    ans = solution.removeElement(nums, val)
    # print(ans)
    print(nums[:ans])