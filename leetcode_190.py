class Solution:
    def reverse_bits(self, n):
        res = 0
        while n > 0:
            lastbit = n & 1
            n = n >> 1
            res = res * 2 + lastbit
        return res

    def reverseBits2(self, n):
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n >> i) & 0x1
        return reversed

    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
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
    # x = 64
    # x = 0b00000010100101000001111010011100
    x = 0b11111111111111111111111111111101
    res2 = sol.reverseBits2(x)
    res = sol.reverseBits(x)
    print(res == res2)
    sol.print_bits(res)
