class Solution:
    def longestDiverseString(self, a, b, c, aa="a", bb="b", cc="c"):
        if a < b:
            return self.longestDiverseString(b, a, c, bb, aa, cc)
        if b < c:
            return self.longestDiverseString(a, c, b, aa, cc, bb)
        if b == 0:
            return aa * min(2, a)
        use_a = min(2, a)
        use_b = 1 if a - use_a >= b else 0
        return (
            aa * use_a
            + bb * use_b
            + self.longestDiverseString(a - use_a, b - use_b, c, aa, bb, cc)
        )


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

if __name__ == "__main__":
    sol = Solution()
    a, b, c = 1, 1, 7
    res = sol.longestDiverseString(a, b, c)
    print("ans is : ", res)
