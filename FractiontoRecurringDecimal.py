import collections
from SerializeDeserializebinaryTree import BinaryTreeSerializer

from helpers.TreeNode import TreeNode
from helpers.BinaryTreeSerializer import BinaryTreeSerializer


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator * denominator < 0 else ""
        result = [sign + str(n), "."]
        remainders = {}

        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))

        if remainder in remainders:
            idx = remainders[remainder]
            result.insert(idx, "(")
            result.append(")")

        return "".join(result).rstrip(".")


if __name__ == "__main__":
    sol = Solution()
    res = sol.fractionToDecimal(1, 6)
    print("Ans is: ", res)
