class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(', '{', '['}
        pair = {'()', '{}', '[]'}
        stack = []
        for x in s:
            if x in left:
                stack.append(x)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top + x in pair:
                    continue
                else:
                    return False
        if stack:
            return False
        return True

if __name__== '__main__':
    solution = Solution()

    s = '([)]'
    ans = solution.isValid(s)
    print(ans)