"""
249. Group Shifted Strings
Medium

1314

245

Add to List

Share
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
"""

import collections
from math import floor
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shift_letter(ch, shift):
            return chr((ord(ch) - shift) % 26 + ord("a"))

        # Create a hash value
        def get_hash(string: str):
            # Calculate the number of shifts to make the first character to be 'a'
            shift = ord(string[0])
            return "".join(shift_letter(letter, shift) for letter in string)

        # Create a hash_value (hashKey) for each string and append the string
        # to the list of hash values i.e. mapHashToList["abc"] = ["abc", "bcd"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)

        # Return a list of all of the grouped strings
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    res = sol.groupStrings(strings)
    print("Ans is: ", res)
