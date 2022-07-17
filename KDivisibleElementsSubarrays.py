from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        B = 201
        n = len(nums)
        power = [0] * 201
        t = 1

        power[0] = 1
        for i in range(1, n):
            power[i] = power[i - 1] * B
        ret = 0
        for l in range(1, n + 1):
            hash = 0
            count = 0
            Set = set()
            for i in range(n):
                # ...i
                if i >= l:
                    hash = hash - nums[i - l] * power[l - 1]
                    count -= nums[i - l] % p == 0

                hash = hash * B + nums[i]
                count += nums[i] % p == 0

                if i >= l - 1:
                    if hash in Set:
                        continue
                    Set.add(hash)
                    if count <= k:
                        ret += 1
                # print('len=',l,i,'(',nums[i],'),hash=',hash,'ret=',ret)
        return ret


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 3, 2, 2]
    res = sol.countDistinct(nums)
    print(res)
