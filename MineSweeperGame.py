"""

"""

from itertools import islice
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dt = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dt2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        def mines(x, y):
            # check 8 dirs num of mines
            ret = 0
            for dx, dy in dt + dt2:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == "M":
                    ret += 1
            return ret

        q = [(click)]
        vis = set()
        while q:
            x, y = q.pop(0)
            if board[x][y] == "E":
                num_m = mines(x, y)
                board[x][y] = "B" if num_m == 0 else str(num_m)
            elif board[x][y] == "M":
                board[x][y] = "X"
            for dx, dy in dt:
                nx, ny = x + dy, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if (nx, ny) in vis:
                    continue
                vis.add((nx, ny))
                if board[x][y] in ["E", "M"]:
                    q.append((nx, ny))


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    click = [3, 0]
    res = sol.updateBoard(board, click)
    print(res)
