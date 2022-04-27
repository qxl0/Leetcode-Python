"""
3. Longest Substring Without Repeating Characters
Medium

22485

1007

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.
"""


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


class Solution2:
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and l <= seen[c]:
                l = seen[c] + 1
            else:
                longest = max(longest, i - l + 1)
            seen[c] = i
        return longest


if __name__ == "__main__":
    sol = Solution3()
    # s = "abcabcbb"
    # s = "bbbb"
    # s = "dvdf"
    # s = "pwwkew"
    # s = "tmmzuxt"
    s = "abcabcbb"
    maxlen = sol.lengthOfLongestSubstring(s)
    print("Max len is:", maxlen)
