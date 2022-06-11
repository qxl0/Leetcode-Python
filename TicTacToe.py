class TicTacToe:
    def __init__(self, n: int):
        self.grid = [[0] * n for _ in range(n)]
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        if self.grid[row][col] == 0:
            self.grid[row][col] = player

        for i in range(self.size):
            if self.grid[row][i] != player:
                break
            if i == self.size - 1:
                return player
        for i in range(self.size):
            if self.grid[i][col] != player:
                break
            if i == self.size - 1:
                return player
        for i in range(self.size):
            if self.grid[i][i] != player:
                break
            if i == self.size - 1:
                return player
        for i in range(self.size):
            if self.grid[i][self.size - 1 - i] != player:
                break
            if i == self.size - 1:
                return player
        return 0


if __name__ == "__main__":
    sol = TicTacToe(3)
    sol.move(0, 0, 1)
    sol.move(0, 2, 2)
    sol.move(2, 2, 1)
    sol.move(1, 1, 2)
    sol.move(2, 0, 1)
    sol.move(1, 0, 2)
    res = sol.move(2, 1, 1)
    print(res)
