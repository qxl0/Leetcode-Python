from calendar import c
from typing import List


class TrieNode:
    def __init__(self):
        self.children, self.is_word = {}, False

    @staticmethod
    def construct_trie(words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                node.children.setdefault(c, TrieNode())
                node = node.children[c]
            node.is_word = True
        return root


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        score, cals = 0, sum(calories[0:k])
        if cals > upper:
            score += 1
        if cals < lower:
            score -= 1

        for i in range(k, len(calories)):
            cals = cals + calories[i] - calories[i - k]
            if cals > upper:
                score += 1
            if cals < lower:
                score -= 1

        return score


if __name__ == "__main__":
    sol = Solution()
    calories = [1, 2, 3, 4, 5]
    res = sol.dietPlanPerformance(calories, k, 3, 3)
    print(res)
