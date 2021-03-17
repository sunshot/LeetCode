class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i+1][j+1] indicates the minimum number of steps required to make word1[0..i] and word2[0..j] the same.
        # dp[0][0] = 0
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for j in range(len(word2)):
            dp[0][j+1] = j+1
        for i in range(len(word1)):
            dp[i+1][0] = i+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
        # print(dp)
        return dp[-1][-1]
        
if __name__== '__main__':
    solution = Solution()

    word1 = "leetcode"
    word2 = "etco"

    ans = solution.minDistance(word1, word2)
    print(ans)