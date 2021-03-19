from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digi_letter = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        if not digits or len(digits) == 0:
            return []
        if len(digits) == 1:
            return digi_letter[digits[0]]
        ans = []
        
        def backtrack(index: int, path: List[str]) -> None:
            # if current path is the same length as digits, then it is one ans
            if len(path) == len(digits):
                ans.append(''.join(path))
                return
            
            letters = digi_letter[digits[index]]
            for letter in letters:
                # Add the letter to our current path
                path.append(letter)
                # Move to next digi
                backtrack(index + 1, path)
                # Then we need to remove letter and move to next
                path.pop()
        
        
        backtrack(0, [])
        
        return ans

if __name__== '__main__':
    solution = Solution()

    digits = '279'
    ans = solution.letterCombinations(digits)
    print(ans)
