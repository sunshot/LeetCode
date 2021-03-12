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
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        # print(d)
        i = 0
        ans = 0
        while i < len(s):
            if s[i:i+2] in d:
                ans += d[s[i:i+2]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans

if __name__== '__main__':
    solution = Solution()

    s = "MCMXCIV"
    ans = solution.romanToInt(s)
    print(ans)