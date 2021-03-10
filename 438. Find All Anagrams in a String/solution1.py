from typing import List
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_hash = collections.Counter(p)
        n = len(p)
        curr_hash = collections.Counter(s[0:n])
        isLastAnagram = False
        ans = []
        if curr_hash == p_hash:
            isLastAnagram = True
            ans.append(0)
        for i in range(1, len(s)-n+1):
            if isLastAnagram and s[i+n-1] == s[i-1]:
                isLastAnagram = True
                ans.append(i)
            else:
                curr_hash[s[i-1]] -= 1
                if curr_hash[s[i-1]] == 0:
                    del curr_hash[s[i-1]]
                curr_hash[s[i+n-1]] += 1
                if curr_hash == p_hash:
                    isLastAnagram = True
                    ans.append(i)
                else:
                    isLastAnagram = False
            # print(curr_hash)
        return ans
        
if __name__== '__main__':
    solution = Solution()

    s = "cbaebabacd"
    p = "abc"
    result = solution.findAnagrams(s, p)
    print(result)