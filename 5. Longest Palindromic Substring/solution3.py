class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s
        result = ''
        max_len = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if 1 > max_len:
                max_len = 1
                result = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if 2 > max_len:
                    max_len = 2
                    result = s[i:i+2]
        for j in range(2, n):
            for i in range(j-1):
                # detect s[i]..s[j]
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        result = s[i:j+1]
        return result

if __name__== '__main__':
    solution = Solution()

    result = solution.longestPalindrome('ababababababa')
    print(result == 'ababababababa')

    result = solution.longestPalindrome('bananas')
    print(result == 'anana')