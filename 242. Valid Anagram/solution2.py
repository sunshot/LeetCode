class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        s_sort = "".join(sorted(s))
        t_sort = "".join(sorted(t))
        
        return s_sort == t_sort
        
if __name__== '__main__':
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)