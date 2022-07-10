"""

"""

from itertools import islice
from typing import List
from sortedcontainers import SortedDict


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dt = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        q = [(click)]
        vis = set()
        vis.add((click[0], click[1]))
        while q:
            # print(q)
            x, y = q.pop(0)
            count = 0
            nxt = []
            for dx, dy in dt:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == "M":
                    count += 1
                else:
                    nxt.append((nx, ny))

            if count == 0:
                board[x][y] = "B"
                for nx, ny in nxt:
                    if (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append((nx, ny))
            else:
                board[x][y] = str(count)

        return board


if __name__ == "__main__":
    sol = Solution()
    # board = [
    #     ["E", "E", "E", "E", "E"],
    #     ["E", "E", "M", "E", "E"],
    #     ["E", "E", "E", "E", "E"],
    #     ["E", "E", "E", "E", "E"],
    # ]
    # click = [3, 0]
    board = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    click = [1, 2]
    res = sol.updateBoard(board, click)
    print(res)
