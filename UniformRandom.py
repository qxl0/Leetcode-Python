"""
"""


import collections
import random
from typing import List


def zero_one_random():
    return random.randrange(2)


class Solution:
    def uniformRandom(self, lower_bound, upper_bound):
        number_of_outcomes = upper_bound - lower_bound + 1
        while True:
            result, i = 0, 0
            while (1 << i) < number_of_outcomes:
                result = (result << 1) | zero_one_random()
                i += 1
            if result < number_of_outcomes:
                break
        return result + lower_bound


if __name__ == "__main__":
    sol = Solution()
    left = 1
    right = 6
    res = sol.uniformRandom(left, right)
    print("result is: ", res)
    res = sol.uniformRandom(left, right)
    print("result is: ", res)
    res = sol.uniformRandom(left, right)
    print("result is: ", res)
