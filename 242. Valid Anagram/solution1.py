import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        s_hash = collections.defaultdict(int)
        t_hash = collections.defaultdict(int)
        
        for i in range(len(s)):
            s_hash[s[i]] += 1
            t_hash[t[i]] += 1
        
        if len(s_hash) != len(t_hash):
            return False
        
        for x in s_hash:
            if s_hash[x] != t_hash[x]:
                return False
        
        return True
        
if __name__== '__main__':
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)