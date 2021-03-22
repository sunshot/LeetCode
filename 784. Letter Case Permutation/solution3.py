from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        ans = []
        
        # backtrack
        def backtrack(path: str, index: int) -> None:
            if index == n:
                ans.append(path)
                return
            
            if S[index].isdigit():
                backtrack(path + S[index], index + 1)
            else:
                backtrack(path + S[index], index + 1)
                backtrack(path + S[index].swapcase(), index + 1)
                
        backtrack('', 0)
        return ans
                  
if __name__== '__main__':
    solution = Solution()

    S = 'a1b2'
    ans = solution.letterCasePermutation(S)
    print(ans)