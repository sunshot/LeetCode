class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        
if __name__== '__main__':
    solution = Solution()

    s = "badc"
    t = "baba"
    result = solution.isIsomorphic(s, t)
    print(result)