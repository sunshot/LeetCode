from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i+1])
        result = 0
        for i, curr in enumerate(height):
            minH = min(leftmax[i], rightmax[i])
            if minH > curr:
                result += minH - curr
        return result
        
if __name__== '__main__':
    solution = Solution()
    
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height)
    print(result == 6)