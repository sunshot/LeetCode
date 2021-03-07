class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result = 0
        stringIndex = {}
        start = 0
        for i in range(len(s)):
            if s[i] in stringIndex and stringIndex[s[i]] >= start:
                # find repeat string s[i], need to reset start index from previous s[i] + 1
                start = stringIndex[s[i]] + 1
            else:
                result = max(result, i-start+1)
            stringIndex[s[i]] = i 
        return result
    
if __name__== '__main__':
    solution = Solution()

    s = 'ababcd'
    result = solution.lengthOfLongestSubstring(s)
    print(result)