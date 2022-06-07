from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ret = []

        def findMax(nums, k):
            # keep non-increasing sequence
            drop = len(nums) - k
            ret = []
            for n in nums:
                while drop > 0 and len(ret) > 0 and n > ret[-1]:
                    drop -= 1
                    ret.pop()
                ret.append(n)
            return ret[:k]

        def merge(p1, p2):
            ret = []
            total = len(p1) + len(p2)
            for i in range(total):
                if p1 > p2:
                    ret.append(p1.pop(0))
                else:
                    ret.append(p2.pop(0))
            return ret

        for i in range(k + 1):
            if i > len(nums1):
                continue
            if k - i > len(nums2):
                continue
            p1 = findMax(nums1, i)
            p2 = findMax(nums2, k - i)
            print(i, p1, p2)
            temp = merge(p1, p2)
            print(temp)
            ret = max(ret, temp)

        return ret


if __name__ == "__main__":
    sol = Solution()
    # nums1 = [8, 6, 9]
    # nums2 = [1, 7, 5]
    # k = 3
    nums1 = [8, 1, 8, 8, 6]
    nums2 = [4]
    k = 2
    res = sol.maxNumber(nums1, nums2, k)
    print(res)
