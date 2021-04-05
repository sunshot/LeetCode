class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        start = len(s) - 1
        while start >= 0:
            # Let's find the longest valid parentheses start from end
            if s[start] == '(':
                start -= 1
                continue
            
            stack = []
            cn = 0
            for i in range(start, -1, -1):
                if s[i] == ')':
                    stack.append((s[i], i))
                else:
                    if not stack or stack[-1][0] == '(':
                        ans = max(ans, cn)
                        start = start - 1
                        break
                    else:
                        cn += 2
                        stack.pop()
            if stack:
                cn = start - stack[0][1]
            ans = max(ans, cn)
            start = start - 1
        return ans

if __name__== '__main__':
    solution = Solution()

    s = "()(()"
    ans = solution.longestValidParentheses(s)
    print(ans)