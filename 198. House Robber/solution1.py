from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_endwith_curr = nums[0]
        max_endwithout_curr = 0
        best_max = max_endwith_curr
        for i in range(1,len(nums)):
            curr_endwith_curr = max_endwithout_curr + nums[i]
            curr_endwithout_curr = max(max_endwith_curr, max_endwithout_curr)
            max_endwith_curr = curr_endwith_curr
            max_endwithout_curr = curr_endwithout_curr
            best_max = max(best_max, max_endwith_curr, max_endwithout_curr)
        return best_max

if __name__== '__main__':
    solution = Solution()

    nums = [2,7,9,3,1]
    ans = solution.rob(nums)
    print(ans == 12)