class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isStringPalindrome(s):
            s_re = s[::-1]
            if s == s_re:
                return True
            return False
            
        if not s or len(s) <= 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        result = ''
        isPalindrom = False
        start = 0
        isEqualPalindrom = False
        i = 1
        while i < len(s):
            if isPalindrom:
                if isEqualPalindrom and s[i] == s[i-1]:
                    i += 1
                    continue
                elif start >=1 and s[i] == s[start-1]:
                    start = start - 1
                    isEqualPalindrom = False
                else:
                    if i-start > len(result):
                        result = s[start:i]
                    reUse = False
                    while start < i:
                        if isStringPalindrome(s[start:i+1]):
                            reUse = True
                            break
                        start += 1
                    if not reUse:
                        i -= 1
                        isPalindrom = False
                        isEqualPalindrom = False
            else:
                if s[i] == s[i-1]:
                    isPalindrom = True
                    isEqualPalindrom = True
                    start = i-1
                elif i>=2 and s[i] == s[i-2]:
                    isPalindrom = True
                    isEqualPalindrom = False
                    start = i-2
            i += 1
        if isPalindrom:
            if i-start > len(result):
                result = s[start:i+1]
        if not result:
            result = s[0]
        return result
    
if __name__== '__main__':
    solution = Solution()

    result = solution.longestPalindrome('ababababababa')
    print(result == 'ababababababa')

    result = solution.longestPalindrome('bananas')
    print(result == 'anana')