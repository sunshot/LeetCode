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
        res = self.letterCombinations(digits[0:len(digits)-1])
        ans = []
        for left in res:
            for right in digi_letter[digits[len(digits)-1]]:
                ans.append(left + right)
        return ans
        

if __name__== '__main__':
    solution = Solution()

    digits = '279'
    ans = solution.letterCombinations(digits)
    print(ans)