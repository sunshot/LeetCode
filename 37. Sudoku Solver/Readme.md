# [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

```
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
```

Constraints:

- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.

Solution1: 失败，打算使用直接解数独的方法，判断行、列、小正方形，但依然会有解不了的情况，真实数独解的时候确实还会增加其他的排除，比如区域排除。本打算增加回溯方法，没有想清楚如何恢复现场，失败。


Solution2: See
https://leetcode.com/problems/sudoku-solver/discuss/15959/Accepted-Python-solution
https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking


Solution3: DFS 其实也是回溯，但是判断是否合法、恢复现场很巧妙。Runtime: 116 ms, faster than 87.08% of Python3 online submissions for Sudoku Solver. 参考的 accepted 里面运行时间考前的答案

回溯最关键的思路：

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```

如何寻找下一个 candidate？如果这个 candidate 不满足要求，如何恢复现场？

最早失败的 Solution1 没有想清楚这点，每次 backtrack 时重新 copy 一份 board，时间复杂度和空间复杂度非常高，其实只需要将失败的 row col 对应的 board 置为 '.' 即可，同理对于判断是否 valid 也是如此，可以与solution3类似，修改hash
