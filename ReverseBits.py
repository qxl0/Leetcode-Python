class Solution:
    def reverse_bits(self, x):
        word_size = 16
        bit_mask = 0xFFFF

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
    sol.print_bits(x)
