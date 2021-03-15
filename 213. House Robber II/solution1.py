from typing import List
class Solution:
    def rob_simple(self, nums: List[int]) -> int:
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
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob_simple(nums[0:n-1]), self.rob_simple(nums[1:n]))
        
if __name__== '__main__':
    solution = Solution()

    nums = [2,3,2]
    ans = solution.rob(nums)
    print(ans == 3)