import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        if len(s1) > len(s2):
            return False
        s1_hash = collections.Counter(s1)
        n = len(s1)
        curr_hash = collections.Counter(s2[0:n])
        if curr_hash == s1_hash:
            return True
        for i in range(1, len(s2)-n+1):
            curr_hash[s2[i-1]] -= 1
            if curr_hash[s2[i-1]] == 0:
                del curr_hash[s2[i-1]]
            curr_hash[s2[i+n-1]] += 1
            if curr_hash == s1_hash:
                return True
        return False
        
if __name__== '__main__':
    solution = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    result = solution.checkInclusion(s1, s2)
    print(result)
