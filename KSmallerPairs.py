import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        ans = []
        q = []
        l1len, l2len = len(nums1), len(nums2)
        if l1len == 0 or l2len == 0 or k == 0:
            return ans
        i = 0
        while i < l1len and i < k:
            heapq.heappush(q, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
            i += 1

        while k and q:
            k -= 1
            print(f"{q}")
            _, n1, n2, idx = heapq.heappop(q)
            ans.append([n1, n2])
            if idx == l2len - 1:
                continue
            heapq.heappush(q, (n1 + nums2[idx + 1], n1, nums2[idx + 1], idx + 1))

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 9
    res = sol.kSmallestPairs(nums1, nums2, k)
    print("res is: ", res)
