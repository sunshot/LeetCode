class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ss = (s + s)[1:-1]
        return s in ss

if __name__== '__main__':
    solution = Solution()

    s = "aabccaabcc"
    result = solution.repeatedSubstringPattern(s)
    print(result)