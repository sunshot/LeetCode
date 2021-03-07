from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = [{} for _ in range(9)]
        colHash = [{} for _ in range(9)]
        boxHash = [{} for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # i is row, j is col
                digi = board[i][j]
                if digi != '.':
                    if digi in rowHash[i]:
                        return False
                    rowHash[i][digi] = 1
                    if digi in colHash[j]:
                        return False
                    colHash[j][digi] = 1
                    index = (i//3) * 3 + j//3
                    if digi in boxHash[index]:
                        return False
                    boxHash[index][digi] = 1
        return True

if __name__== '__main__':
    solution = Solution()

    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solution.isValidSudoku(board))