class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] = longest palindrome subsequence of s[i to j].
        # If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
        # Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        if not s:
            return 0
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 if i+1 <= j-1 else 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

if __name__== '__main__':
    solution = Solution()

    s = "bbab"
    result = solution.longestPalindromeSubseq(s)
    print(result)