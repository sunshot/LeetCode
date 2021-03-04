import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ''
        left = 0
        right = 0
        t_char_hash = collections.defaultdict(int)
        curr_hash = collections.defaultdict(int)
        for x in t:
            t_char_hash[x] += 1
        required = len(t_char_hash)
        formed = 0
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        filter_s = []
        for i, c in enumerate(s):
            if c in t_char_hash:
                filter_s.append((i, c))
                
        while right < len(filter_s):
            c = filter_s[right][1]
            curr_hash[c] += 1
            if curr_hash[c] == t_char_hash[c]:
                formed += 1
            
            # Try to contract and expand the window
            while left <= right and formed == required:
                c = filter_s[left][1]
                # Save the smallest window until now.
                start = filter_s[left][0]
                end = filter_s[right][0]
                if end + 1 - start < ans[0]:
                    ans = (end + 1 - start, start, end)
                curr_hash[c] -= 1
                if curr_hash[c] < t_char_hash[c]:
                    formed -= 1
                left += 1
            right += 1
        if ans[0] == float("inf"):
            return ""
        else:
            return s[ans[1]:ans[2]+1]

if __name__== '__main__':
    solution = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)