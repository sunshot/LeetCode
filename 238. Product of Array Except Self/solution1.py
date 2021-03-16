from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cn = 0
        total_product = 1
        for num in nums:
            if num == 0:
                zero_cn += 1
            else:
                total_product *= num
        if zero_cn > 1:
            return [0] * len(nums)
        result = []
        for num in nums:
            if num == 0:
                result.append(total_product)
            elif zero_cn == 1:
                result.append(0)
            else:
                result.append(total_product//num)
        return result
                
        
if __name__== '__main__':
    solution = Solution()

    nums = [1,2,3,4]
    ans = solution.productExceptSelf(nums)
    print(ans)