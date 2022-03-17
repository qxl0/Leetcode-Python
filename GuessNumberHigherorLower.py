class Solution:
    def guessNumber(self, n):
        lo, hi = 1, n
        mid = (lo + hi) >> 1
        while (res := guess(mid)) != 0:
            # continue guess
            if res == -1:
                hi = mid - 1
            else:
                lo = mid + 1
            mid = (lo + hi) >> 1
        return mid


def guess(n):
    C = 2
    if n > C:
        return -1
    elif n < C:
        return 1
    return 0


if __name__ == "__main__":
    sol = Solution()
    # n = 10
    n = 2
    res = sol.guessNumber(n)
    print("the number is: ", res)
