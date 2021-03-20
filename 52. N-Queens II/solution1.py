class Solution:
    def totalNQueens(self, n: int) -> int:
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
        
        def backtrack_nqueen(row = 0, count = 0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    visited.append((row, col))
                    rows.add(row)
                    cols.add(col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                        # print(visited)
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    visited.remove((row, col))
                    rows.discard(row)
                    cols.discard(col)
            return count
        
        return backtrack_nqueen(0, 0)

if __name__== '__main__':
    solution = Solution()

    n = 4
    ans = solution.totalNQueens(n)
    print(ans)