from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7

        n = len(arr)
        ret = 0
        # count = Counter(arr)
        count = [0] * 101
        for a in arr:
            count[a] += 1
        # print(count)
        for i in range(target + 1):
            for j in range(i + 1, target + 1):
                k = target - i - j
                if k < 0 or k > 100 or k < j:
                    continue
                if not count[i] or not count[j] or not count[k]:
                    continue
                if i == j and j == k:
                    ret += (count[i] - 2) * (count[i] - 1) * count[i] // 6
                elif i == j and j != k:
                    ret += count[i] * (count[i] - 1) // 2 * count[k]
                elif i != j and j == k:
                    ret += count[i] * (count[j] - 1) * count[j] // 2
                else:
                    ret += count[i] * count[j] * count[k]
        return ret % MOD


if __name__ == "__main__":
    sol = Solution()
    arr = ([1, 1, 2, 2, 2, 2],)
    target = 5
    res = sol.threeSumMulti(arr, target)
    print("Ans is: ", res)
