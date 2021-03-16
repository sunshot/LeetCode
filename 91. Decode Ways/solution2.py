class Solution:    
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            #solution up to i, not including i
            if 0 < int(s[i-1]) < 10:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]
        
if __name__ == '__main__':
    solution = Solution()

    # s = "226"
    # s = "11106"
    s = "111111111111111111111111111111111111111111111"
    ans = solution.numDecodings(s)
    print(ans == 1836311903)