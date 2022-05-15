from collections import Counter, defaultdict
from re import S
import sys
from typing import List


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        window = Counter()
        for i in range(len(s)):
            window[s[i]] += 1
            while len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            ans = max(ans, i - left + 1)
        return ans


class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n * k == 0:
            return 0

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1

        while right < n:
            # add new character and move right pointer
            hashmap[s[right]] = right
            right += 1

            if len(hashmap) == k + 1:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len


if __name__ == "__main__":
    sol = Solution2()
    s = "eceba"
    k = 2
    res = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(res)
