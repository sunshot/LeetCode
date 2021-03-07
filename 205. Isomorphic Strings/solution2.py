class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        smapt = {}
        tmaps = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a in smapt and smapt[a] != b:
                return False
            smapt[a] = b
            if b in tmaps and tmaps[b] != a:
                return False
            tmaps[b] = a
        return True

if __name__== '__main__':
    solution = Solution()

    s = "badc"
    t = "baba"
    result = solution.isIsomorphic(s, t)
    print(result)