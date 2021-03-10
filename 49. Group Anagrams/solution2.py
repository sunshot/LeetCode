from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for x in strs:
            ans[tuple(sorted(x))].append(x)
        return ans.values()

if __name__== '__main__':
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    ans = solution.groupAnagrams(strs)
    print(ans)

