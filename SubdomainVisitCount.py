"""
811. Subdomain Visit Count
Medium

1062

1117

Add to List

Share
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.
"""


from calendar import c
import collections
from math import floor
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            ct, domain = domain.split(" ")
            count = int(ct)
            frags = domain.split(".")
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return [f"{ct} {dom}" for dom, ct in ans.items()]


if __name__ == "__main__":
    sol = Solution()
    cpdomains = ["9001 discuss.leetcode.com"]
    res = sol.subdomainVisits(cpdomains)
    print(res)
