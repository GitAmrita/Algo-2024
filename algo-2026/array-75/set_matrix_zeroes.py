from collections import defaultdict
from typing import List   
def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1
    zero_row = set()
    zero_col = set()

    def make_zero(val, is_row_modified):
        if is_row_modified:
            for col in range(cols + 1):
                matrix[val][col] = 0
        else:
            for row in range(rows + 1):
                matrix[row][val] = 0


    for i in range(rows + 1):
        for j in range(cols + 1):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for v in list(zero_row):
        make_zero(v, True)
    for v in list(zero_col):
        make_zero(v, False)