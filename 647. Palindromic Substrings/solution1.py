class Solution:
    def expand(self, s: str, left:int, right:int, palind) -> str:
        while left>=0 and right<len(s) and s[left] == s[right]:
            palind.add((left, right))
            left -= 1
            right += 1
        return s[left+1:right]
    def countSubstrings(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 1
        # record start and end index for any valid palindrom substring
        palind = set()
        for i in range(len(s)):
            self.expand(s, i, i, palind)
            self.expand(s, i, i+1, palind)
        return len(palind)

if __name__== '__main__':
    solution = Solution()

    s = "aaabaaaca"
    expected = 19
    result = solution.countSubstrings(s)
    print(result == expected)