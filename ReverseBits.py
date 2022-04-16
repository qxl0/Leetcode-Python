class Solution:
    def reverse_bits(self, x):
        word_size = 32
        bit_mask = 0xFFFFFFFF
        res = 0
        for _ in range(word_size):
            res = (res << 1) + (x & 1)
            x >>= 1
        return res

    def print_bits(self, x):
        lst = []
        original = x
        while x:
            tmp = x & 1
            lst.append(tmp)
            x >>= 1
        while len(lst) < 32:
            lst.append(0)
        lst = lst[::-1]
        res = " ".join(str(e) for e in lst)
        print(res)


if __name__ == "__main__":
    sol = Solution()
    # x = 64
    # x = 0b00000010100101000001111010011100
    x = 2**31 - 1
    sol.print_bits(x)
    res = sol.reverse_bits(x)
    sol.print_bits(res)
