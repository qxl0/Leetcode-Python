"""
556. Next Greater Element III
Medium

2198

346

Add to List

Share
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
"""


class Solution:
    def nextGreaterElements(self, n):
        s = list(str(n))

        fst = -1
        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                fst = i
                break
        if fst == -1:
            return -1

        scd = -1

        for i in range(len(s) - 1, -1, -1):
            if s[i] > s[fst]:
                scd = i
                break
        s[fst], s[scd] = s[scd], s[fst]
        s[fst + 1 :] = s[fst + 1 :][::-1]
        ans = int("".join(s))
        return ans if ans < 2147483648 else -1


if __name__ == "__main__":
    sol = Solution()
    # n = 158476531
    n = 230241
    res = sol.nextGreaterElements(n)

    print(res)
