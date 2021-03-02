class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        if n == m:
            if needle == haystack:
                return 0
            else:
                return -1
            
        lps = [0] * m
        i = 1
        index = 0
        while i < m:
            if needle[i] == needle[index]:
                index += 1
                lps[i] = index
                i += 1
            else:
                if index != 0:
                    index = lps[index-1]
                else:
                    lps[i] = 0
                    i += 1
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == m:
                return i-j
            elif i < n and haystack[i] != needle[j]:
                # Do not match lps[0..lps[j-1]] characters, 
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                
        return -1

if __name__== '__main__':
    solution = Solution()

    haystack = 'hello'
    needle = 'll'
    result = solution.strStr(haystack, needle)
    print(result == 2)