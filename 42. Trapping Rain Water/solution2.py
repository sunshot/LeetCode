from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        stack = []
        result = 0
        for i, curr in enumerate(height):
            while stack and curr > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(curr, height[stack[-1]]) - height[top]
                result += distance * bounded_height
            stack.append(i)
        return result

if __name__== '__main__':
    solution = Solution()
    
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # expected = 6
    height = [4,2,0,3,2,5]
    expected = 9
    result = solution.trap(height)
    print(result == expected)
