import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = collections.Counter(s)
        t_hash = collections.Counter(t)
        
        return s_hash == t_hash

if __name__== '__main__':
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)