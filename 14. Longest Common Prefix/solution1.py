from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs or not strs[0]:
            return prefix
        for i in range(len(strs[0])):
            curr = None
            for x in strs:
                if i >= len(x):
                    return prefix
                if curr == None:
                    curr = x[i]
                elif curr != x[i]:
                    return prefix
            prefix += curr
        return prefix

if __name__== '__main__':
    solution = Solution()

    strs = ["flower","flow","flight"]
    ans = solution.longestCommonPrefix(strs)
    print(ans)