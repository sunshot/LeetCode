import collections
class Solution:
    def containsChar(self, curr_hash: dict(), t_char_hash: dict()) -> bool:
        for x in t_char_hash:
            if x not in curr_hash or curr_hash[x] < t_char_hash[x]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ''
        left = 0
        right = 0
        t_char_hash = collections.defaultdict(int)
        curr_hash = collections.defaultdict(int)
        for x in t:
            t_char_hash[x] += 1
        result = ''
        isFind = False
        while right < len(s):
            curr_hash[s[right]] += 1
            if not self.containsChar(curr_hash, t_char_hash):
                right += 1
            else:
                # We find the window
                isFind = True
                result = s[left:right+1]
                break
        if not isFind:
            return ''
        # We find the first window
        while right < len(s):
            if isFind:
                # contract
                if s[left] not in t_char_hash or curr_hash[s[left]] > t_char_hash[s[left]]:
                    # contract and still statisfy
                    curr_hash[s[left]] -= 1
                    left += 1
                    if right+1 - left < len(result):
                        result = s[left:right+1]
                else:
                    isFind = False
                    curr_hash[s[left]] -= 1
                    left += 1
            else:
                # expend
                right += 1
                if right < len(s):
                    curr_hash[s[right]] += 1
                    if self.containsChar(curr_hash, t_char_hash):
                        isFind = True
        while isFind and left < right:
            if s[left] not in t_char_hash or curr_hash[s[left]] > t_char_hash[s[left]]:
                curr_hash[s[left]] -= 1
                left += 1
                if right+1 - left < len(result):
                    result = s[left:right+1]
        return result

if __name__== '__main__':
    solution = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)