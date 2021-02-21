class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int, right:int) -> str:
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if not s or len(s) <= 1:
            return s
        result = ''
        for i in range(len(s)):
            # odd case, like aba
            tmp = expand(i, i)
            if len(tmp) > len(result):
                result = tmp
            # even case, like abba
            tmp = expand(i, i+1)
            if len(tmp) > len(result):
                result = tmp
        return result