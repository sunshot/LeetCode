from typing import List
import collections
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowHash = collections.defaultdict(set)
        colHash = collections.defaultdict(set)
        boxHash = collections.defaultdict(set)
        queue = collections.deque([])
        N = 9
        digits = [str(i+1) for i in range(N)]
        
        for row in range(N):
            for col in range(N):
                if board[row][col] != '.':
                    index = (row//3) * 3 + col//3
                    rowHash[row].add(board[row][col])
                    colHash[col].add(board[row][col])
                    boxHash[index].add(board[row][col])
                else:
                    queue.append((row, col))
        
        def dfs():
            if not queue:
                return True
            
            row, col = queue[0]
            index = (row//3) * 3 + col//3
            
            for digi in digits:
                if (digi not in rowHash[row]) and (digi not in colHash[col]) and (digi not in boxHash[index]):
                    board[row][col] = digi
                    rowHash[row].add(digi)
                    colHash[col].add(digi)
                    boxHash[index].add(digi)
                    queue.popleft()
                    
                    if dfs():
                        return True
                    else:
                        board[row][col] = '.'
                        rowHash[row].discard(digi)
                        colHash[col].discard(digi)
                        boxHash[index].discard(digi)
                        queue.appendleft((row, col))
            return False
        
        dfs()

if __name__== '__main__':
    solution = Solution()

    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    solution.solveSudoku(board)
    print(board)