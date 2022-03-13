class Solution:
    def lengthOfLongestSubstring(self, s):
        used = {}
        start = 0
        maxlen = 0
        for i, v in enumerate(s):
            if v in used:
                start = i
                used = {}
                used[v] = i
            else:
                used[v] = i
                maxlen = max(maxlen, i - start + 1)
        return maxlen


if __name__ == "__main__":
    sol = Solution()
    # s = "abcabcbb"
    # s = "bbbb"
    s = "dvdf"
    maxlen = sol.lengthOfLongestSubstring(s)
    print("Max len is:", maxlen)
