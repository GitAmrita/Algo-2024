from typing import List


def exist(self, board: List[List[str]], word: str) -> bool:
    rows = len(board) - 1
    cols = len(board[0]) - 1
    k = 0
    def dfs(i, j, k):
        if k == len(word):
            return True
        seen.add((i, j))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for x, y in directions:
            ni = i + x
            nj = j + y
            if 0 <= ni <= rows and 0 <= nj <= cols:
                if board[ni][nj] == word[k] and (ni, nj) not in seen:
                    if dfs(ni, nj, k + 1):
                        return True
        seen.remove((i, j))
        return False

    for i in range(rows + 1):
        for j in range(cols + 1):
            if board[i][j] == word[k]:
                seen = set()
                if dfs(i, j, 1):
                    return True
    return False