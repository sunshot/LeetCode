from typing import List
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curr_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max_sum = float('-inf')
        curr_min_sum = float('inf')
        for num in A:
            curr_sum += num
            curr_max_sum = max(num, curr_max_sum + num)
            max_sum = max(max_sum, curr_max_sum)
            
            curr_min_sum = min(num, curr_min_sum + num)
            min_sum = min(min_sum, curr_min_sum)
        
        if curr_sum == min_sum:
            return max_sum
        
        max_sum = max(max_sum, curr_sum - min_sum)
        return max_sum

if __name__== '__main__':
    solution = Solution()

    A = [5,-3,5]
    ans = solution.maxSubarraySumCircular(A)
    print(ans)