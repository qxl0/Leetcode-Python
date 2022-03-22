class Solution:
    def reverse_bits(self, x):
        res = 0
        while n > 0:
            lastbit = n & 1
            n = n >> 1
            res = res * 2 + lastbit
        return res

    def print_bits(self, x):
        lst = []
        original = x
        while x:
            tmp = x & 1
            lst.append(tmp)
            x >>= 1
        lst = lst[::-1]
        res = " ".join(str(e) for e in lst)
        print(original, res)


if __name__ == "__main__":
    sol = Solution()
    x = 64
    sol.reverse_bits(x)
