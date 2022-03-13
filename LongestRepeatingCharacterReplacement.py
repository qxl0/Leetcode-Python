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


if __name__ == "__main__":
    sol = Solution()
    # s = "AABABBA"
    # s = "BAAAABBBBBA"
    # s = "ABCDEFG"
    s = "AABABBBB"
    k = 1
    res = sol.LongestRepeatingCharacterReplacement(s, k)
    print("Result is: ", res)
