from typing import List, Optional
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        mostK = counter.most_common(k)
        return [item for item, count in mostK]

    def topKFrequent2(self, nums, k):
        hs = {}
        frq = {}

        for i in range(len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z, v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        arr = []
        # most freq - len(nums), so loop from high ---> 0 if in frq, append it
        for x in range(len(nums), 0, -1):
            if x in frq:
                for i in frq[x]:
                    arr.append(i)
        return [arr[x] for x in range(k)]

    def topKFrequent3(self, nums, k):
        frq = collections.defaultdict(list)
        c = collections.Counter(nums)
        for key, cnt in c.items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k:
                return res[:k]
        return res[:k]


if __name__ == "__main__":
    s = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    nums = [3, 0, 1, 0]
    k = 1
    res = s.topKFrequent(nums, k)
    print(res)
