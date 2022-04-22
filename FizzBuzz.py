"""
412. Fizz Buzz
Easy

346

63

Add to List

Share
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


import collections
from typing import List, Optional
from helpers.TreeNode import TreeNode


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        pass


if __name__ == "__main__":
    sol = Solution()
    n = 3
    res = sol.fizzBuzz(n)
    print(res)
