class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) <= 1:
            return s
        if numRows <= 1:
            return s
        n = len(s)
        m = (numRows-1) * (n//(numRows*2-2)+1)
        zigzag = [[None]*m for _ in range(numRows)]
        col = 0
        index = 0
        for i in range(n//(numRows*2-2)):
            # first numRows col
            for theRow in range(numRows):
                zigzag[theRow][col] = s[index]
                index += 1
            col += 1
            for theRow in range(numRows-2, 0, -1):
                zigzag[theRow][col] = s[index]
                index += 1
                col += 1
        theRow = 0
        while theRow < numRows and index < n:
            zigzag[theRow][col] = s[index]
            index += 1
            theRow += 1
        col += 1
        theRow = numRows-2
        while theRow > 0 and index < n:
            zigzag[theRow][col] = s[index]
            index += 1
            theRow -= 1
            col += 1
        # print(zigzag)
        result = ''
        for i in range(numRows):
            for j in range(m):
                if zigzag[i][j]:
                    result += zigzag[i][j]
        return result

if __name__== '__main__':
    solution = Solution()

    s = 'PAYPALISHIRING'
    numRows = 3
    result = solution.convert(s, numRows)
    print(result == 'PAHNAPLSIIGYIR')