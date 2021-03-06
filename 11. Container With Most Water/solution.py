from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
            
if __name__== '__main__':
    solution = Solution()
    
    height = [1,3,2,5,25,24,5]
    result = solution.maxArea(height)
    print(result == 24)