from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        n = len(tiles)
        tiles.sort()
        presum = [0] * n
        presum[0] = tiles[0][1] - tiles[0][0] + 1
        for i in range(1, n):
            presum[i] = presum[i - 1] + tiles[i][1] - tiles[i][0] + 1

        ret = 0
        j = 0
        for i in range(n):
            while j < n and tiles[i][0] + carpetLen - 1 >= tiles[j][1]:
                j += 1
            if i == 0:
                l = presum[j - 1]
            else:
                l = presum[j - 1] - presum[i - 1]
            if j < n:
                l += max(0, tiles[i][0] + carpetLen - 1 - tiles[j][0] + 1)
            ret = max(ret, l)

        return ret


if __name__ == "__main__":
    sol = Solution()
    tiles = [[3, 4], [1, 2]]
    carpetLen = 1
    res = sol.maximumWhiteTiles(tiles, carpetLen)
    print(res)
