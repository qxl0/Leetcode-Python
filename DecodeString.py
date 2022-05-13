"""
394. Decode String
Medium

8025

343

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
"""


from math import floor
from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        def decode():
            s = []
            while stack and stack[-1] != "[":
                s.append(stack.pop())
            s = s[::-1]
            stack.pop()
            num = []
            while stack and stack[-1].isdigit():
                num.append((stack.pop()))
            num = num[::-1]
            t = int("".join(num))
            stack.append("".join(s) * t)

        for ch in s:
            if ch == "]":
                decode()
                continue
            stack.append(ch)
        return "".join(stack)


class Solution2:
    def decodeString(self, s):
        if not s or len(s) == 0:
            return s
        result, position = self.dfs(0, s, 0, "")
        return result

    def dfs(self, position, s, prev_num, prev_str):
        while position < len(s):
            while s[position].isdigit():
                prev_num = prev_num * 10 + int(s[position])
                position += 1

            if s[position] == "[":
                # reset the prev_str
                returned_str, ending_pos = self.dfs(
                    position + 1, s, prev_num=0, prev_str=""
                )
                # backtrack
                prev_str = prev_str + returned_str * prev_num
                position = ending_pos
                prev_num = 0
            # return the result
            elif s[position] == "]":
                return prev_str, position
            else:
                prev_str += s[position]
            position += 1
        return prev_str, position


if __name__ == "__main__":
    sol = Solution2()
    # s = "2[a]2[bc]"
    s = "2[4[2[jk]ef]]"
    res = sol.decodeString(s)

    print(res)
