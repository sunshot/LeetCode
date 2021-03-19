from typing import List
import collections
class Solution:
    def clearUpdateCandidates(sefl, board: List[List[str]], rowHash, colHash, boxHash, candidates) -> None:
        candidates.clear()
        for i in range(len(board)):
            for j in range(len(board[0])):
                # i is row, j is col
                digi = board[i][j]
                if digi == '.':
                    possible = []
                    index = (i//3) * 3 + j//3
                    for x in ['1','2','3','4','5','6','7','8','9']:
                        if x in rowHash[i]:
                            continue
                        if x in colHash[j]:
                            continue
                        if x in boxHash[index]:
                            continue
                        possible.append(x)
                    candidates[(i, j)] = possible

    def updateCandidates(self, board: List[List[str]], rowHash, colHash, boxHash, boxIndex, candidates) -> None:
        while True:
            isFindCandiate = False
            for row_col, possible in candidates.items():
                if len(possible) == 1:
                    i, j = row_col
                    isFindCandiate = True
                    digi = possible[0]
                    board[i][j] = digi
                    rowHash[i].add(digi)
                    colHash[j].add(digi)
                    index = (i//3) * 3 + j//3
                    boxHash[index].add(digi)
            if isFindCandiate:
                self.clearUpdateCandidates(board, rowHash, colHash, boxHash, candidates)
            for index in range(9):
                counter = collections.Counter()
                for row_col in boxIndex[index]:
                    if row_col in candidates:
                        counter.update(candidates[row_col])
                if 1 in counter.values():
                    isFindCandiate = True
                    for digi, value in counter.items():
                        if value == 1:
                            # Let's find digi in which row_col
                            for row_col in boxIndex[index]:
                                if row_col in candidates and digi in candidates[row_col]:
                                    i, j = row_col
                                    board[i][j] = digi
                                    rowHash[i].add(digi)
                                    colHash[j].add(digi)
                                    boxHash[index].add(digi)
                                    del candidates[row_col]
                                    break
            if isFindCandiate:
                # Update candidates
                self.clearUpdateCandidates(board, rowHash, colHash, boxHash, candidates)
            if not isFindCandiate:
                return

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Build valid info
        rowHash = [set() for _ in range(9)]
        colHash = [set() for _ in range(9)]
        boxHash = [set() for _ in range(9)]
        boxIndex = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                # i is row, j is col
                digi = board[i][j]
                if digi != '.':
                    rowHash[i].add(digi)
                    colHash[j].add(digi)
                    index = (i//3) * 3 + j//3
                    boxHash[index].add(digi)
        candidates = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                # i is row, j is col
                digi = board[i][j]
                if digi == '.':
                    index = (i//3) * 3 + j//3
                    boxIndex[index].add((i, j))
                    possible = []
                    for x in ['1','2','3','4','5','6','7','8','9']:
                        if x in rowHash[i]:
                            continue
                        if x in colHash[j]:
                            continue
                        if x in boxHash[index]:
                            continue
                        possible.append(x)
                    candidates[(i, j)] = possible
        self.updateCandidates(board, rowHash, colHash, boxHash, boxIndex, candidates)
        self.isSolved = True
        if len(candidates) > 1:
            # We need backtracking
            self.isSolved = False

if __name__== '__main__':
    solution = Solution()

    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    solution.solveSudoku(board)
    print(board)