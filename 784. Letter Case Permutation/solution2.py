from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        candidates = list(S)
        ans = []
        
        # backtrack
        def backtrack(path: List[int], index: int) -> None:
            if len(path) == len(candidates):
                ans.append(''.join(path))
                return
            if len(path) > len(candidates):
                return
            if index > len(candidates):
                return
            
            # start from index
            for i in range(index, len(candidates)):
                letter = candidates[i]
                if letter.isdigit():
                    path.append(letter)
                    if len(path) == len(candidates):
                        ans.append(''.join(path))
                        return
                else:
                    # add current letter
                    backtrack(path + [letter], i + 1)

                    # add swapcase
                    backtrack(path + [letter.swapcase()], i + 1)
    
        backtrack([], 0)
        return ans
                  
if __name__== '__main__':
    solution = Solution()

    S = 'a1b2'
    ans = solution.letterCasePermutation(S)
    print(ans)