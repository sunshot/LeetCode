from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        # put index to stack
        stack = []      
        n = len(nums)
        ans = [-1] * n
        circular = nums + nums
        
        for i, x in enumerate(circular):
            while stack and circular[stack[-1]] < x:
                # Then stack[-1] next is x
                index = stack.pop() 
                ans[index % n] = x
            stack.append(i)
        return ans

if __name__== '__main__':
    solution = Solution()

    nums = [1,3,4,2]
    expected = [3, 4, -1, 3]

    result = solution.nextGreaterElements(nums)
    print(result == expected)