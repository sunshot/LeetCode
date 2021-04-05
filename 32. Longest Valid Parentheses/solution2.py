class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        stack = []
        for i, x in enumerate(s):
            if x == '(':
                stack.append((x, i))
            else:
                # )
                if not stack or stack[-1][0] == ')':
                    stack.append((x, i))
                else:
                    stack.pop()
        # compute the ans
        if not stack:
            return len(s)
        stack.append(('', len(s)))
        ans = stack[0][1]
        for i in range(1, len(stack)):
            cn = stack[i][1] - stack[i-1][1] - 1
            ans = max(ans, cn)
        return ans
        
if __name__== '__main__':
    solution = Solution()

    s = "()(()"
    ans = solution.longestValidParentheses(s)
    print(ans)