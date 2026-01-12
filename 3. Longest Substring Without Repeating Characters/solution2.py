class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        curr_start = 0
        curr_end = 1

        start = 0
        end = 1

        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                start = s.find(s[end], start, end) + 1
                end += 1
            if end - start > curr_end - curr_start:
                curr_start = start
                curr_end = end
        
        return curr_end - curr_start
