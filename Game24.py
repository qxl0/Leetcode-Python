from typing import List


from itertools import permutations


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(nums, l, r):
            if l == r:
                return set([nums[l]])
            rets = set()
            for i in range(l, r):
                A = helper(nums, l, i)
                B = helper(nums, i + 1, r)
                for x in A:
                    for y in B:
                        rets.add(x + y)
                        rets.add(x - y)
                        rets.add(x * y)
                        if y != 0:
                            rets.add(x / y)
            return rets

        p = permutations(cards)
        for nums in list(p):
            # compute 24 for nums
            rets = helper(nums, 0, 3)
            for x in rets:
                if abs(x - 24) < 1e-10:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    cards = [4, 1, 8, 9]
    res = sol.judgePoint24(cards)
    print(res)
