from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nth_bit = 1 << n
        
        for i in range(2**n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]
            
            # append subset corresponding to that bitmask
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return ans
        
if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3]
    ans = solution.subsets(nums)
    print(ans)