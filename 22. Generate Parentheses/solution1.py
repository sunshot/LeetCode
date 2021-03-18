from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        if n == 2:
            result = []
            result.append('()()')
            result.append('(())')
            return result
        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    ans.append('({}){}'.format(left, right))
        return ans
        
if __name__== '__main__':
    solution = Solution()

    n = 3
    ans = solution.generateParenthesis(n)
    print(ans)

    n = 4
    ans = solution.generateParenthesis(n)
    print(ans)