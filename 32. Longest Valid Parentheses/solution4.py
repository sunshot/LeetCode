class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        left = right = 0
        for x in s:
            if x == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2*left)
            elif left < right:
                left = right = 0
        left = right = 0
        for x in s[::-1]:
            if x == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans,2*left)
            elif left > right:
                left = right = 0
        
        return ans

if __name__== '__main__':
    solution = Solution()

    s = "()(()"
    ans = solution.longestValidParentheses(s)
    print(ans)      
