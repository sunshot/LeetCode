from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])


if __name__== '__main__':
    solution = Solution()

    # nums = [1,3,5,6]
    # target = 5

    nums = [1,3,5,6]
    target = 2

    ans = solution.searchInsert(nums, target)
    print(ans)
        