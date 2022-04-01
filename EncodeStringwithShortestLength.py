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
        pass


if __name__ == "__main__":
    sol = Solution()
    str = "abbbabbbcabbbabbbc"
    res = sol.encode(str)
    print(res)
