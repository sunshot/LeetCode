class Solution:
    def romanToInt(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ans = 0
        last = 0
        for c in s[::-1]:
            if d[c] < last:
                ans -= d[c]
            else:
                ans += d[c]
                last = d[c]
        return ans

if __name__== '__main__':
    solution = Solution()

    s = "MCMXCIV"
    ans = solution.romanToInt(s)
    print(ans)