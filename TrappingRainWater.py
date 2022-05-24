"""
42. Trapping Rain Water
Hard

17728

250

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
"""

from this import d
from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


class Solution2:
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume


class Solution3:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        curr = 0

        while curr < len(height):
            while stack and stack[-1] < height[curr]:
                top = stack.pop()
                if not stack:
                    break
                area += (curr - stack[-1] - 1) * min(height[curr], height[stack[-1]])
            stack.append(curr)
            curr += 1
        return area


if __name__ == "__main__":
    sol = Solution3()
    # height = [4, 2, 0, 3, 2, 5]
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = sol.trap(height)
    print(res)
