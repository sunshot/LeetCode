from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_dict = {}
        
        for x in nums2:
            while stack and stack[-1] < x:
                # Then stack[-1] next is x
                next_dict[stack.pop()] = x
            stack.append(x)
        
        ans = []
        for x in nums1:
            if x in next_dict:
                ans.append(next_dict[x])
            else:
                ans.append(-1)
        
        return ans
        
if __name__== '__main__':
    solution = Solution()

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

    result = solution.nextGreaterElement(nums1, nums2)

    print(result)