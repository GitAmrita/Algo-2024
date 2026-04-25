# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
from typing import List
def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    row_len = len(heights)
    col_len = len(heights[0])
    pacific = set()
    atlantic = set()
    # insert 1st row
    for j in range(0, col_len):
        pacific.add((0, j))
    # insert 1st col
    for i in range(0, row_len):
        pacific.add((i, 0))
            
    # insert last row
    for j in range(col_len):
        atlantic.add((row_len - 1, j))
    # insert last col
    for i in range(row_len):
        atlantic.add((i, col_len - 1))

    def dfs(x, y, ocean):
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # [right, left, bottom, top]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_len and 0 <= ny < col_len:
                if (nx, ny) not in ocean and heights[nx][ny] >= heights[x][y]:
                    ocean.add((nx, ny))
                    dfs(nx, ny, ocean)

    for row, col in list(pacific):
        dfs(row, col, pacific)
    for row, col in list(atlantic):
        dfs(row, col, atlantic)
    return [[r, c] for r, c in pacific & atlantic] 