from collections import Counter
from math import inf
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        ans = 1
        boat = 0
        for i in range(len(people)):
            if boat + people[i] <= limit:
                boat += people[i]
            else:
                boat = people[i]
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 1, 6, 4]
    limit = 7
    res = sol.numRescueBoats(nums, limit)
    print(res)
