import heapq
import random
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


class Solution2:
    def topKFrequent(self, nums, k):
        freq = {}  # n --> freq
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        # set up maxHeap
        h = []
        for n, f in freq.items():
            heapq.heappush(h, (f * (-1), n))
        # pop up top K
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res


class Solution4:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = right  # random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k :]


if __name__ == "__main__":
    s = Solution4()
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    # nums = [3, 0, 1, 0]
    # k = 1
    nums = [4, 5, 5, 2, 1, 1, 1, 5, 2, 3, 3, 5, 2]
    k = 3
    res = s.topKFrequent(nums, k)
    print(res)
