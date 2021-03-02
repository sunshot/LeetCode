class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        n = len(s)
        first = s[0]
        last = s[-1]
        first_reverse_index = n - 1
        while first_reverse_index > 0:
            if s[first_reverse_index] == first:
                # s[first_reverse_index..n-1] is the substring?
                sub = s[first_reverse_index:n]
                if sub == s[0:len(sub)] and n % len(sub) == 0:
                    times = n // len(sub)
                    newstr = sub * times
                    if newstr == s:
                        return True
            first_reverse_index -= 1
        return False

if __name__== '__main__':
    solution = Solution()

    s = "aabccaabcc"
    result = solution.repeatedSubstringPattern(s)
    print(result)