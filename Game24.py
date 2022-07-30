from typing import List


from itertools import permutations


class Solution:
    class Solution:
        def judgePoint24(self, cards: List[int]) -> bool:
            def helper(nums, l, r):
                if l == r:
                    return set([(nums[l], f"{nums[l]}")])
                rets = set()
                for i in range(l, r):
                    A = helper(nums, l, i)
                    B = helper(nums, i + 1, r)
                    for x, x1 in A:
                        for y, y1 in B:
                            rets.add((x + y, f"({x1})+({y1})"))
                            rets.add((x - y, f"({x1})-({y1})"))
                            rets.add((x * y, f"({x1})*({y1})"))
                            if y != 0:
                                rets.add((x / y, f"({x})/({y})"))
                return rets

            p = permutations(cards)
            for nums in list(p):
                # compute 24 for nums
                rets = helper(nums, 0, 3)
                for x, y in rets:
                    if abs(x - 24) < 1e-10:
                        print(y)
                        return True
            return False


if __name__ == "__main__":
    sol = Solution()
    cards = [4, 1, 8, 9]
    res = sol.judgePoint24(cards)
    print(res)
