class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or len(s.strip()) == 0:
            return 0
        txt = s.strip()
        index = txt.rfind(' ') + 1
        return len(txt) - index
        
if __name__== '__main__':
    solution = Solution()
    
    s = " Hello World "
    result = solution.lengthOfLastWord(s)
    print(result)
