"""
885 · Encode String with Shortest Length
Algorithms
Hard
Accepted Rate
43%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
"""


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def encode(self, s):
        # write your code here
        n = len(s)
        f = [[""] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            f[i][i] = s[i]
            for j in range(i + 1, n):
                tmp = s[i : j + 1]
                f[i][j] = tmp

                # prefer original over compressed
                for k in range(i, j):
                    if len(f[i][k]) + len(f[k + 1][j]) < len(f[i][j]):
                        f[i][j] = f[i][k] + f[k + 1][j]

                # compress whole string only for shorter length
                size = len(tmp)
                index = (tmp + tmp).find(tmp, 1)
                if index < size:
                    replace = "%d[%s]" % (
                        size // index,
                        f[i][i + index - 1],
                    )
                    if len(replace) < len(f[i][j]):
                        f[i][j] = replace
        return f[0][n - 1]


if __name__ == "__main__":

    sol = Solution()
    str = "abbbabbbcabbbabbbc"
    # str = "aaaaa"
    res = sol.encode(str)
    print(res)

# %%
