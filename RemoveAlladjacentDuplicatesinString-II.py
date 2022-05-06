class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            elif s[i] != s[i-1]:
              count = 1
            if count == k:
                s = s.replace(s[i - k + 1 : i + 1], "")
                return self.removeDuplicates(s, k)
        return s


if __name__ == "__main__":
    sol = Solution()
    s = "deeedbbcccbdaa"
    k = 3
    res = sol.removeDuplicates(s, k)
    print(res)
