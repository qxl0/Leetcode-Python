"""
93. Restore IP Addresses
Medium

2658

624

Add to List

Share
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
"""


from typing import List, Optional
from helpers.LinkedList import Node


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Do not return anything, modify nums in-place instead.
        """
        ret = []

        def dfs(s, idx, path):
            if idx == 4:
                if not s:
                    ret.append(path[:-1])
                    return
            for i in range(1, 4):
                if i > len(s):
                    continue
                if i > 1 and s[0] == "0":
                    continue
                if i > 2 and int(s[:i]) > 255:
                    continue
                dfs(s[i:], idx + 1, path + s[:i] + ".")

        dfs(s, 0, "")
        return ret


if __name__ == "__main__":
    sol = Solution()
    s = "25525511135"
    res = sol.restoreIpAddresses(s)
    print(res)
