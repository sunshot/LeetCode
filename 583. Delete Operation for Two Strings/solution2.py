class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                if c == d:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
    
    def minDistance(self, word1: str, word2: str) -> int:
        lcs = self.longestCommonSubsequence(word1, word2)
        return len(word1) - lcs + len(word2) - lcs
        
if __name__== '__main__':
    solution = Solution()

    word1 = "leetcode"
    word2 = "etco"

    ans = solution.minDistance(word1, word2)
    print(ans)        