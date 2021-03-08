class Solution:
    def expand(self, s: str, left:int, right:int) -> int:
        result = 0
        while left>=0 and right<len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
        return result
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 1
        ans = 0
        for i in range(len(s)):
            ans += self.expand(s, i, i)
            ans += self.expand(s, i, i+1)
        return ans

if __name__== '__main__':
    solution = Solution()

    s = "aaabaaaca"
    expected = 19
    result = solution.countSubstrings(s)
    print(result == expected)