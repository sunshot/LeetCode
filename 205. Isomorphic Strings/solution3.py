class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) != len(t):
            return False
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        