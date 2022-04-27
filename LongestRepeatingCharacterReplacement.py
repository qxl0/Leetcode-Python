"""
424. Longest Repeating Character Replacement
Medium

4090

162

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


from collections import defaultdict


class Solution:
    def LongestRepeatingCharacterReplacement(self, s, k):
        charCountMap = {}
        left = 0
        maxRepeat, maxWindow = 0, 0

        for i, c in enumerate(s):
            if c not in charCountMap:
                charCountMap[c] = 0
            charCountMap[c] += 1

            maxRepeat = max(maxRepeat, charCountMap[c])
            if i - left + 1 - maxRepeat > k:
                c = s[left]
                charCountMap[c] -= 1
                if charCountMap[c] == 0:
                    charCountMap.pop(c, None)
                left += 1
            maxWindow = max(maxWindow, i - left + 1)

        return maxWindow


class Solution2:
    def LongestRepeatingCharacterReplacement(self, s: str, k: int) -> int:
        max_length = max(1, k)
        counts = defaultdict(int)
        counts[s[0]] += 1
        l = 0

        for r in range(1, len(s)):
            counts[s[r]] += 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

    def LongestRepeatingCharacterReplacement2(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        counter[s[0]] += 1
        l = 0
        maxlen = 0
        for i, c in enumerate(s[1:], 1):
            counter[c] += 1
            while i - l + 1 - max(counter.values()) > k:
                counter[s[l]] -= 1
                l -= 1
            maxlen = max(maxlen, i - l + 1)
        return maxlen


if __name__ == "__main__":
    sol = Solution2()
    # s = "AABABBA"
    # s = "BAAAABBBBBA"
    # s = "ABCDEFG"
    s = "AABABBA"
    k = 1
    res = sol.LongestRepeatingCharacterReplacement2(s, k)
    print("Result is: ", res)
