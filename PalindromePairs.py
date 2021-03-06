from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def palindromePairs(self, words):
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[: i + 1] == word[: i + 1][::-1]:
                    valid_suffixes.append(word[i + 1 :])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for word_index, word in enumerate(words):
            reversed_word = word[::-1]

            # Build solutions of case #1. This word will be word 1.
            if (
                reversed_word in word_lookup
                and word_index != word_lookup[reversed_word]
            ):
                solutions.append([word_index, word_lookup[reversed_word]])

            # Build solutions of case #2. This word will be word 2.
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], word_index])

            # Build solutions of case #3. This word will be word 1.
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([word_index, word_lookup[reversed_prefix]])

        return solutions


class Solution2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        m = {w: i for i, w in enumerate(words)}

        def ispar(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        ans = []
        for j in range(n):
            s = words[j]

            # split to YYY YYYY
            for k in range(len(s) + 1):
                s1 = s[:k]
                s2 = s[k:]

                # s1 par, s2 reversed
                s2r = s2[::-1]
                if ispar(s1) and s2r != s and s2r in m:
                    print("1", j, s, s2, s2r)
                    ans.append([m[s2r], j])

                # s2 par, s1 reversed
                if len(s1) == len(s):
                    continue
                s1r = s1[::-1]
                if ispar(s2) and s1r != s and s1r in m:
                    print("2", j, s, s1, s1r)
                    ans.append([j, m[s1r]])
        return ans


if __name__ == "__main__":
    s = Solution2()
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    # words = ["lls", "sssll"]
    # words = ["a", ""]
    res = s.palindromePairs(words)
    print(res)
