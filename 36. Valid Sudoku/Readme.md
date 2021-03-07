# 36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
1. Each column must contain the digits 1-9 without repetition.
1. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Solution

利用 Hash 或者 Set 记录出现的数字，即每一行、每一列、每一个3x3都需要一个hash，问题的难点在于，如何根据 行号 i (0-8)，列号 j (0-8) 判断出 3x3 的序号 (0-8)？

```python
index = (i//3) * 3 + j//3
```

参考解答：

````
One could use box_index = (row / 3) * 3 + col / 3 where / is an integer division, row is a row number, and col is a column number.
````
