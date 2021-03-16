from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans[i] indicates product of 0..i-1
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            if i != n-1:
                right = right * nums[i+1]
            ans[i] = right * ans[i]
        return ans
                
if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3,4]
    ans = solution.productExceptSelf(nums)
    print(ans)