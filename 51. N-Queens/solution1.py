from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        rows = set()
        cols = set()
        visited = []
        def is_not_under_attack(row, col) -> bool:
            if not visited:
                return True
            if row in rows:
                return False
            if col in cols:
                return False
            for row_col in visited:
                i, j = row_col
                if abs(i - row) == abs(j - col):
                    return False
            return True
        
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
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    visited.append((row, col))
                    rows.add(row)
                    cols.add(col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        addSolution()
                        # print(visited)
                    else:
                        # we move on to the next row
                        backtrack_nqueen(row + 1)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    visited.remove((row, col))
                    rows.discard(row)
                    cols.discard(col)
        
        backtrack_nqueen(0)
        return ans


if __name__== '__main__':
    solution = Solution()

    n = 4
    ans = solution.solveNQueens(n)
    print(ans)