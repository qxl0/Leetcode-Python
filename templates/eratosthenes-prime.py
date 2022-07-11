from math import sqrt


class Solution:
    def eratosthenes(self, n):
        q = [0] * (n + 1)
        primes = []

        for i in range(2, int(sqrt(n)) + 1):
            if q[i] == 1:
                continue
            j = i * 2
            while j <= n:
                q[j] = 1
                j += i
        for i in range(2, n + 1):
            if q[i] == 0:
                primes.append(i)
        return primes


if __name__ == "__main__":
    sol = Solution()
    res = sol.eratosthenes(20)
    print(res)
