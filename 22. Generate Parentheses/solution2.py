from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(A: List[str], s: str, left: int, right: int) -> None:
            if len(s) == 2*n:
                A.append(s)
                return
            if left < n:
                backtrack(A, s + '(', left + 1, right)
            if right < left:
                backtrack(A, s + ')', left, right + 1)
        
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        A = []
        backtrack(A, '', 0, 0)
        return A

if __name__== '__main__':
    solution = Solution()

    n = 3
    ans = solution.generateParenthesis(n)
    print(ans)

    n = 4
    ans = solution.generateParenthesis(n)
    print(ans)