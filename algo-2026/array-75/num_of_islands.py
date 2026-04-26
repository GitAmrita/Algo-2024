# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from typing import List
def numIslands(self, grid: List[List[str]]) -> int:
    num_island = 0
    visited = set()
    row_len = len(grid) 
    col_len = len(grid[0])
    def dfs(x, y):
        visited.add((x, y))
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] # [left, right, bottom, top]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_len and 0 <= ny < col_len:
                if grid[nx][ny] == "1" and (nx, ny) not in visited:
                    dfs(nx, ny)
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == "1" and (i, j) not in visited:
                num_island += 1
                dfs(i, j)
    return num_island