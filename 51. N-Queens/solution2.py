from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        diag1 = set()
        diag2 = set()
        visited = []
        
        def addSolution() -> None:
            sol = []
            for row_col in visited:
                curr = ['.'] * n
                i, j = row_col
                curr[j] = 'Q'
                sol.append(''.join(curr))
            ans.append(sol)
        
        def backtrack_nqueen(row = 0) -> None:
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
                        addSolution()
                        # print(visited)
                    else:
                        # we move on to the next row
                        backtrack_nqueen(row + 1)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    visited.remove((row, col))
                    cols.discard(col)
                    diag1.discard(row+col)
                    diag2.discard(row-col)
        
        backtrack_nqueen(0)
        return ans


if __name__== '__main__':
    solution = Solution()

    n = 8
    ans = solution.solveNQueens(n)
    print(ans)