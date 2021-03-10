from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = [None] * len(strs)
        for i, x in enumerate(strs):
            dicts[i] = collections.Counter(x)
        ans = []
        isAdded = [False] * len(strs)
        for i in range(len(strs)):
            if not isAdded[i]:
                isAdded[i] = True
                curr = [strs[i]]
                for j in range(i+1, len(strs)):
                    if not isAdded[j] and dicts[i] == dicts[j]:
                        isAdded[j] = True
                        curr.append(strs[j])
                ans.append(curr)
        return ans

if __name__== '__main__':
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    ans = solution.groupAnagrams(strs)
    print(ans)