from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n

        firstbit = xor & (~(xor - 1))

        num1 = 0
        for n in nums:
            if n & firstbit:
                num1 ^= n
        num2 = num1 ^ xor
        return [num1, num2]


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 3, 4]
    res = sol.singleNumber(nums)
    print("Ans is: ", res)
