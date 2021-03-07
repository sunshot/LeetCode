import itertools
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(s)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(t)]
        smapt = {}
        tmaps = {}
        if len(g1) != len(g2):
            return False
        for a, b in zip(g1, g2):
            if a[1] != b[1]:
                return False
            if a[0] in smapt and smapt[a[0]] != b[0]:
                return False
            smapt[a[0]] = b[0]
            if b[0] in tmaps and tmaps[b[0]] != a[0]:
                return False
            tmaps[b[0]] = a[0]
        return True
        
if __name__== '__main__':
    solution = Solution()

    s = "badc"
    t = "baba"
    result = solution.isIsomorphic(s, t)
    print(result)