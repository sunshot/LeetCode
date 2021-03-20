class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()
        diag2 = set()
        visited = []
        
        def backtrack_nqueen(row = 0, count = 0):
            for col in range(n):
                # iterate through columns at the curent row.
                if (col not in cols) and (row+col not in diag1) and (row-col not in diag2):
                    # explore this partial candidate solution, and mark the attacking zone
                    visited.append((row, col))
                    cols.add(col)
                    diag1.add(row+col)
                    diag2.add(row-col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                        # print(visited)
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    visited.remove((row, col))
                    cols.discard(col)
                    diag1.discard(row+col)
                    diag2.discard(row-col)
            return count
        
        return backtrack_nqueen(0, 0)
        
if __name__== '__main__':
    solution = Solution()

    n = 4
    ans = solution.totalNQueens(n)
    print(ans)