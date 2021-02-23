class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) <= 1:
            return s
        if numRows <= 1:
            return s
        n = len(s)
        cycleLen = 2*numRows-2
        result = ''
        for i in range(numRows):
            j = 0
            while j+i < n:
                result += s[j+i]
                if i!=0 and i!=numRows-1 and j+cycleLen-i < n:
                    result += s[j+cycleLen-i]
                j += cycleLen
        return result
            