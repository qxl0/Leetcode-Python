class Solution:
    def countDigitOne(self, n: int) -> int:
        N = len(str(n))
        count = 0
        # 345[Y]78
        for i in range(1, N + 1):
            f = n // int(pow(10, i))
            count += f * int(pow(10, i - 1))

            digit = (n - f * pow(10, i)) // pow(10, i)
            if digit > 1:
                count += pow(10, i - 1)
            elif digit == 1:
                last = n - f * pow(10, i) % pow(10, i - 1)
                count += last
        return count


if __name__ == "__main__":
    sol = Solution()
    n = 13
    res = sol.countDigitOne(n)
    print("Ans is: ", res)
