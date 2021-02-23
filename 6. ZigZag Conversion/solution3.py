class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) <= 1:
            return s
        if numRows <= 1:
            return s
        ## https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
        L = [''] * numRows
        index = step = 0
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)