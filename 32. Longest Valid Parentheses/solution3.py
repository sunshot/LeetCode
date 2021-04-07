class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        ans = 0
        for i, x in enumerate(s):
            if not stack:
                stack.append(i)
                continue
            if x == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
      
if __name__== '__main__':
    solution = Solution()

    s = "()(()"
    ans = solution.longestValidParentheses(s)
    print(ans)  
